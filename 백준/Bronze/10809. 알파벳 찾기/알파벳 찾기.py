s=input()
ans=[-1]*26
for i in range(len(s)):
     if  ans[ord (s[i])-97] == -1 : ans[ord (s[i])-97]=i
print(ans[0],end='')
for i in range(1,26):
     print (" %d"%ans[i],end='')
