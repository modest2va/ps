import sys
n=int(sys.stdin.readline())
ans=[0]*(n+1)
imposter=list(map(int, sys.stdin.readline().split()))
for i in imposter:
    ans[i]+=1
ans[0]=0
mymax=max(ans)
cnt=0
for i in range(len(ans)):
    if ans[i]==mymax: cnt+=1
if cnt!=1: print('skipped')
else:
    for i in range(len(ans)):
        if ans[i] == mymax: print(i);break