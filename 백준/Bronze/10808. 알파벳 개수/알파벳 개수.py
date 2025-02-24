s=input()
ans=[0]*26
for i in range(len(s)):
     ans[ord (s[i])-97]+=1
print(ans[0],end='')
for i in range(1,26):
     print (" %d"%ans[i],end='')
