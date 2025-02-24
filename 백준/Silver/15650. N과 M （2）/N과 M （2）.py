n,m=map(int,input().split())
s=[]
ans=[]
def dfs():
    if len(s)==m:
        tmpAns=sorted((map(int,s)))
        if tmpAns not in ans :ans.append(tmpAns)
        return
    for i in range(1, n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
dfs()

for i in ans:
    print(*i)