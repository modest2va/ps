n=int(input())
ans=n
for i in range(n):
    tmp=input()
    if list(tmp)!=sorted(tmp, key=tmp.find): ans-=1
print(ans)