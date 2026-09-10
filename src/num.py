import io,re
P='sa.html'; s=io.open(P,encoding='utf-8').read()
# cover counts as page 1; every .ft gets 2,3,4...
n=[1]
def rep(m):
    n[0]+=1
    return m.group(1)+'%02d'%n[0]+m.group(3)
s=re.sub(r'(<div class="ft">.*?<span>)([^<]*)(</span></div>)', rep, s, flags=re.S)
io.open(P,'w',encoding='utf-8').write(s)
print('numbered through page', n[0])
