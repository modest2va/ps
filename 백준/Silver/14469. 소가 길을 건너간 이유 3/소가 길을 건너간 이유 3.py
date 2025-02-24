import sys
n=int(sys.stdin.readline())
tmp=[]
for i in range(n):
    a,b=map(int, sys.stdin.readline().split())
    tmp.append((a,b))
tmp.sort(key= lambda x: (x[0],x[1]))
ans=0
for i in tmp:
    if i[0] >ans: ans= i[0]+i[1]
    else: ans+=i[1]
print(ans)