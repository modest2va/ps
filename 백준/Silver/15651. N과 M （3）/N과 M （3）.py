n,m=map(int,input().split())
s=[]
def dfs():
    if len(s)==m:
        tmp=(" ".join(map(str, s)))
        print(tmp)
        return
    for i in range(1,n+1):
        s.append(i)
        dfs()
        s.pop()
dfs()