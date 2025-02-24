import sys
for _ in range(int(sys.stdin.readline())):
    n,a,b=map(int,sys.stdin.readline().split())
    mytarget=bin (min(a,b))[2:]
    cnt=0
    for i in range(len(mytarget)):
        if mytarget[i]=='1' : cnt=i
    cnt=len(mytarget)-cnt
    print(n-cnt+1)