import sys
cnta=0
cntb=0
for _ in range(int(sys.stdin.readline())):
    a,b=map(int,sys.stdin.readline().split())
    if a>b: cnta+=1
    elif a<b: cntb+=1
print("%d %d"%(cnta,cntb))