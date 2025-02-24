s=int(input())
ans=''
while s!=0:
    ans+=str(s%2)
    s//=2
print(ans[::-1])