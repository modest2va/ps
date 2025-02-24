tmp=[1,1,2,2,2,8]
ans=list(map(int,input().split()))
for i in range(6):
    if i!=5:
        print(tmp[i]-ans[i],end=" ")
    else : print(tmp[i]-ans[i])
