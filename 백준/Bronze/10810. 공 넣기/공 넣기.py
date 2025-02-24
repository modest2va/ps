import sys
m,n=map(int,sys.stdin.readline().split())
tmp=[0]*m
for _ in range(n):
    a,b,c=map(int,sys.stdin.readline().split())
    for i in range(a,b+1):
        tmp[i-1]=c
print(tmp[0],end='')
for i in range(1,len(tmp)):
    print(" %d"%tmp[i],end='')