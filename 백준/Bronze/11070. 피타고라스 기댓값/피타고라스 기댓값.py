import sys
for _ in range(int(sys.stdin.readline())):
    n,m=map(int, sys.stdin.readline().split())
    getscores,losescores=[0]*n,[0]*n
    for i in range(m):
        a,b,p,q=map(int, sys.stdin.readline().split())
        getscores[a-1]+=p ; losescores[a-1]+=q
        getscores[b-1]+=q; losescores[b-1]+=p
    ans=[]
    for i in range(n):
        if getscores[i]**2+losescores[i]**2!=0:
            ans.append(getscores[i]**2/(getscores[i]**2+losescores[i]**2))
        else: ans.append(0)
    print(int (max(ans)*1000))
    print(int(min(ans) * 1000))