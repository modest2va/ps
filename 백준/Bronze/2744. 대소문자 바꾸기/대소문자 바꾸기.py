import sys
s=sys.stdin.readline()
ans=''
for i in range(len(s)-1):
    if s[i].isupper() ==True : ans+=s[i].lower()
    else: ans+=s[i].upper()
print(ans)