import io,re,pathlib
from playwright.sync_api import sync_playwright
P='sa.html'
def load(): return io.open(P,encoding='utf-8').read()
def save(x): io.open(P,'w',encoding='utf-8').write(x)
JS="""()=>[...document.querySelectorAll('.pg[data-fit]')].map(el=>{
  const bd=el.querySelector('.bd');
  if(!bd) return {over:0, slack:0};
  let max=0; bd.querySelectorAll('.m>p,.fig,.rail,.box,.bet,table,h2,h4').forEach(n=>{
    const q=n.getBoundingClientRect(); if(q.bottom>max)max=q.bottom;});
  const r=bd.getBoundingClientRect();
  return {over: Math.round(bd.scrollHeight-bd.clientHeight), slack: Math.round(r.bottom-max)};
})"""
with sync_playwright() as pw:
    b=pw.chromium.launch(channel='chrome')
    pg=b.new_page(viewport={'width':1240,'height':1754})
    def measure():
        pg.goto(pathlib.Path(P).resolve().as_uri()); pg.wait_for_timeout(420)
        return pg.evaluate(JS)
    step=0
    for step in range(30):
        m=measure(); s=load()
        parts=re.split(r'(--fs:[0-9.]+pt)', s)
        fs=[float(x[5:-2]) for x in parts[1::2]]
        assert len(fs)==len(m), (len(fs),len(m))
        changed=False
        for i,info in enumerate(m):
            if info['over']>1 and fs[i]>9.4: fs[i]=round(fs[i]-0.1,1); changed=True
            elif info['over']<=1 and info['slack']>105 and fs[i]<10.1: fs[i]=round(fs[i]+0.1,1); changed=True
        for j,v in enumerate(fs): parts[1+2*j]='--fs:%.1fpt'%v
        save(''.join(parts))
        if not changed: break
    m=measure()
    over=[i+1 for i,x in enumerate(m) if x['over']>1]
    hole=[(i+1,x['slack']) for i,x in enumerate(m) if x['slack']>140]
    print('steps',step+1); print('OVERFLOW pages:', over or 'none'); print('HOLES >24mm:', hole or 'none')
    b.close()
