import sys
n=int(sys.stdin.readline())
for _ in range(n):
    tmp=list(map(int, sys.stdin.readline().split()))
    ans=0
    oddtmp=[]
    for i in range(7):
       if tmp[i]%2==0: ans+=tmp[i]; oddtmp.append(tmp[i])
    print("%d %d"%(ans,min(oddtmp)))
