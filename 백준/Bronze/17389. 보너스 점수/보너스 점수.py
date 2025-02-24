n=int(input())
ans=0
cnt=0
s=input()
for i in range( n):
    if s[i]=='X' : cnt=0
    else: ans+=i+1+cnt ; cnt+=1
print(ans)