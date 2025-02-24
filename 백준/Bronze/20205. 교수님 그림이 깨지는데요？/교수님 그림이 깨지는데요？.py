import sys
n,k=map(int, sys.stdin.readline().split())
for i in range(n):
    ans=[]
    tmp=list(map(int, sys.stdin.readline().split()))
    for j in range(len(tmp)):
        for _ in range(k):
          ans.append(tmp[j])
    for j in range(k):
        print(*ans)