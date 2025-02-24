#print(ord('A')-55)
s=input().split()
n,b=s[0],int(s[1])
ans=0
for i in range(len(n)):
     if n[len(n)-i-1].isupper(): ans+=(ord(n[len(n)-i-1])-55)*pow(b,i)
     else :  ans+=int(n[len(n)-i-1])*pow(b,i)
print(ans)