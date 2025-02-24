import sys
for _ in range(int(sys.stdin.readline())):
    n,k=map(int, sys.stdin.readline().split())
    cnt=0
    tmp=list(map(int,sys.stdin.readline().split()))
    for i in range(n):
        cnt+=tmp[i]//k
    print(cnt)