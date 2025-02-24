import sys
a,b=map(int,sys.stdin.readline().split())
tmp=list(map(int,sys.stdin.readline().split()))
for i in range(a):
    tmp[i]%=b
cnt=tmp[0]
for i in range(1,a):
    cnt*=tmp[i]
print(cnt%b)