import sys
while 1:
    n=int(sys.stdin.readline())
    if n==-1: break
    permile=[]
    tmptime=[0]
    time=[]
    ans=0
    for i in range(n):
        a,b=map(int, sys.stdin.readline().split())
        permile.append(a)
        tmptime.append(b)
    for i in range(n):
        time.append(tmptime[i+1]-tmptime[i])
    for i in range(n):
        ans+=permile[i]*time[i]
    print("%d miles"%ans)