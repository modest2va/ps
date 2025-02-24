n=int(input())
tmp=list(map(int, input().split()))
mysum=[]
mysum.append(tmp[0])
ans=0
for i in range(1,n):
    mysum.append(mysum[i-1]+tmp[i])
for i in range(n):
    ans+=tmp[i]*(mysum[n-1]-mysum[i])
print(ans)