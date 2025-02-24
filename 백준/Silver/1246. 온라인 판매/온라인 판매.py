n,m=map(int, input().split())
tmp=[]
for i in range(m):
    tmp.append(int(input()))
tmp.sort()
price,ans=0,0
for i in range(m):
    mymax=min(m-i,n)
    if ans< tmp[i]*mymax: price=tmp[i]; ans=tmp[i]*mymax
print(price,ans)