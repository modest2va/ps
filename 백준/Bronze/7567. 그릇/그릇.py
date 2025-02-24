import sys
s=sys.stdin.readline()
ans=10
for i in range(1,len(s)-1):
    if s[i]==s[i-1]: ans+=5
    else : ans+=10
print(ans)