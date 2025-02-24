import sys
for _ in range(int(sys.stdin.readline())):
    d,n,s,p=map(int,sys.stdin.readline().split())
    if n*s<d+n*p: print("do not parallelize")
    elif n * s > d + n * p: print("parallelize")
    elif n * s == d + n * p: print("does not matter")