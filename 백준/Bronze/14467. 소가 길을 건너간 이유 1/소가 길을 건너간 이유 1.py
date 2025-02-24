ans=[[] for i in range(10)]
n=int(input())
cnt=0
for i in range(n):
    idx,gil=map(int,input().split())
    idx-=1
    ans[idx].append(gil)
for i in range(10):
    if len(ans[i])>1:
        for j in range(len(ans[i])-1):
            if ans[i][j]!=ans[i][j+1] : cnt+=1
    else :pass
print(cnt)