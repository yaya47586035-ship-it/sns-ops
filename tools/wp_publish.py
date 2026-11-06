"""디피로그 워드프레스 업로드 (인증은 프록시가 주입). 사용:
python3 wp_publish.py 콘텐츠폴더 --status draft|publish
콘텐츠폴더/01_difilog_post.html 상단 주석에서 제목·슬러그·카테고리·태그·요약을 읽음.
"""
import re,sys,json,os,subprocess,argparse,urllib.parse
ap=argparse.ArgumentParser();ap.add_argument('dir');ap.add_argument('--status',default='draft');a=ap.parse_args()
B='https://blog.difizone.com/wp-json/wp/v2'
def curl(args):
    r=subprocess.run(['curl','-sS','-A','Mozilla/5.0']+args,capture_output=True,text=True)
    try: return json.loads(r.stdout)
    except: raise SystemExit('bad response: '+r.stdout[:500]+r.stderr)
src=open(os.path.join(a.dir,'01_difilog_post.html'),encoding='utf-8').read()
head=re.search(r'<!--(.*?)-->',src,re.S).group(1)
def f(k): return re.search(rf'^\s*{k}:\s*(.+)$',head,re.M).group(1).strip()
title=f('제목');slug=f('슬러그\(고유주소\)');cat=f('카테고리');tags=[t.strip() for t in f('태그').split(',')];excerpt=f('요약\(메타 설명\)')
body=src[src.index('-->')+3:].strip()
st=os.path.join(a.dir,'wp_state.json');S=json.load(open(st)) if os.path.exists(st) else {}
# duplicate check
ex=curl([f'{B}/posts?slug={urllib.parse.quote(slug)}&status=publish,draft,pending,future,private&context=edit&_fields=id,status,link'])
if ex and not S.get('post_id'): raise SystemExit(f'이미 같은 슬러그 글 있음: {ex}')
def upload(path,alt):
    name=os.path.basename(path)
    r=curl(['-X','POST',f'{B}/media','-H',f"Content-Disposition: attachment; filename*=UTF-8''{urllib.parse.quote(name)}",'-H','Content-Type: image/png','--data-binary','@'+path])
    if 'id' not in r: raise SystemExit(f'upload fail {r}')
    curl(['-X','POST',f'{B}/media/{r["id"]}','-H','Content-Type: application/json','-d',json.dumps({'alt_text':alt})])
    return r['id'],r['source_url']
img=os.path.join(a.dir,'images')
if 'thumb' not in S:
    S['thumb']=upload([os.path.join(img,x) for x in os.listdir(img) if x.endswith('-thumb.png')][0],title)
if 'body' not in S:
    S['body']=upload([os.path.join(img,x) for x in os.listdir(img) if x.endswith('-body.png')][0],title+' 관련 이미지')
json.dump(S,open(st,'w'))
body=body.replace('{{본문이미지URL}}',S['body'][1])
assert '{{' not in body, '치환 안 된 {{ }} 있음'
cats=curl([f'{B}/categories?per_page=100&_fields=id,name']);cid=[c['id'] for c in cats if c['name']==cat]
if not cid: raise SystemExit('카테고리 없음 '+cat)
tids=[]
for t in tags:
    r=curl([f'{B}/tags?search={urllib.parse.quote(t)}&_fields=id,name'])
    m=[x['id'] for x in r if x['name']==t]
    if not m:
        r=curl(['-X','POST',f'{B}/tags','-H','Content-Type: application/json','-d',json.dumps({'name':t})]); m=[r['id']]
    tids.append(m[0])
data={'title':title,'slug':slug,'status':a.status,'categories':cid,'tags':tids,'featured_media':S['thumb'][0],'excerpt':excerpt,
      'content':'<!-- wp:html -->\n'+body+'\n<!-- /wp:html -->'}
url=f"{B}/posts/{S['post_id']}" if S.get('post_id') else f'{B}/posts'
r=curl(['-X','POST',url,'-H','Content-Type: application/json','--data-binary','@-'] ) if False else None
p=subprocess.run(['curl','-sS','-A','Mozilla/5.0','-X','POST',url,'-H','Content-Type: application/json','--data-binary','@-'],input=json.dumps(data),capture_output=True,text=True)
r=json.loads(p.stdout)
if 'id' not in r: raise SystemExit(f'post fail {p.stdout[:500]}')
S['post_id']=r['id'];S['status']=r['status'];S['link']=r['link'];json.dump(S,open(st,'w'),ensure_ascii=False)
print(json.dumps({'id':r['id'],'status':r['status'],'link':r['link'],'preview':f"https://blog.difizone.com/?p={r['id']}&preview=true"},ensure_ascii=False))
