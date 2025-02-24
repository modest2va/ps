import sys
for _ in range(int(sys.stdin.readline())):
    n,d= map(int, sys.stdin.readline().split())
    cnt=0
    for i in range(n):
        a,b,c,=map(int,sys.stdin.readline().split())
        if a*(b/c)>=d: cnt+=1
    print(cnt)