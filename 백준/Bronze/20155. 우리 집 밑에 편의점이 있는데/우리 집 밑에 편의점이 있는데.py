import sys
n,m=map(int, sys.stdin.readline().split())
tmp=list(map(int, sys.stdin.readline().split()))
ans=[0]*(m+1)
for i in tmp:
    ans[i]+=1
print(max(ans))