import sys
while True:
    tmp=sys.stdin.readline()
    if not (tmp) : break
    n,k=map(int, tmp.split())
    s=n
    while n//k:
        s=s+n//k
        n=n//k+n%k
    print(s)