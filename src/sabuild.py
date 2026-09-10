from playwright.sync_api import sync_playwright
import pathlib, sys, fitz, numpy as np, PIL.Image as I
OUT = r'C:\Users\zzhua\Desktop\被允许动的钱_金融科技的下一个十年.pdf'
with sync_playwright() as p:
    b=p.chromium.launch(channel='chrome')
    pg=b.new_page(viewport={'width':1240,'height':1754})
    pg.goto(pathlib.Path('sa.html').resolve().as_uri()); pg.wait_for_timeout(900)
    JS="""()=>[...document.querySelectorAll('.pg')].map((el,i)=>{
      const bd=el.querySelector('.bd'); if(!bd) return {p:i+1,over:0};
      return {p:i+1, over: Math.round(bd.scrollHeight-bd.clientHeight)};})"""
    bad=[x for x in pg.evaluate(JS) if x['over']>1]
    print('OVERFLOW:', bad or 'none')
    n=pg.evaluate("()=>document.querySelectorAll('.pg').length")
    print('pages in html:', n)
    if '--shots' in sys.argv:
        for i in range(n): pg.locator('.pg').nth(i).screenshot(path='s%02d.png'%(i+1))
    pg.pdf(path=OUT, format='A4', print_background=True,
           margin={'top':'0','right':'0','bottom':'0','left':'0'})
    b.close()
d=fitz.open(OUT); print('pdf pages', d.page_count)
for i,page in enumerate(d):
    px=page.get_pixmap(dpi=100); px.save('q%02d.png'%(i+1))
    im=np.array(I.open('q%02d.png'%(i+1)).convert('L')); h,w=im.shape
    rows=(im<200).sum(axis=1)/w; top,bot=int(h*.05),int(h*.94); band=rows[top:bot]
    run=best=0;pos=0
    for k,v in enumerate(band):
        if v<0.004: run+=1
        else:
            if run>best: best,pos=run,k-run
            run=0
    if run>best: best,pos=run,len(band)-run
    print('p%02d ink=%.1f%% gap=%.0fmm@%.0f%%'%(i+1,band.mean()*100,best/h*297,(top+pos)/h*100))
