import sys
n,q = map(int,sys.stdin.readline().split())
tmp=[0]
cnt=0
for i in range(n):
    cnt+= int(sys.stdin.readline())
    tmp.append(cnt)
for i in range(q):
    test=int(sys.stdin.readline())
    for _ in range(len(tmp)):
        if tmp[_]<= test and test <tmp[_+1]: print(_+1)