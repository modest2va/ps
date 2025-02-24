import sys
n,k=map(int ,input().split())
tmp=list(map(int,sys.stdin.readline().split()))
mymax=-1*999999
for i in range(len(tmp)-k+1):
    mymax=max(mymax,sum(tmp[i:i+k]))
print(mymax)