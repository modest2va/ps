import sys
tmp=[]
for i in range(31):
    tmp.append(2**i)
n=int(sys.stdin.readline())
cnt=0
for _ in range(31):
    if n== tmp[_]:cnt=1; print(cnt); break
if cnt==0 :print(cnt)
