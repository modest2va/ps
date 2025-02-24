scores=[[],[],[]]
n=int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    scores[0].append(a)
    scores[1].append(b)
    scores[2].append(c)
ans=[]
for i in range(n):
    res=0
    for j in range(3):
        if scores[j].count(scores[j][i])==1 : res+=scores[j][i]
    ans.append(res)
for i in ans:
    print(i)