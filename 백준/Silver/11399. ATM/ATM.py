N=int(input())
a= list(map(int,input().split()))
ans=0
a.sort()
for _ in range(N):
   ans+=a[_]*(N-_)
print (ans)
