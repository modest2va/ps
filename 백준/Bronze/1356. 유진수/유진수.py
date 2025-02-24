s=input()
ans=0
for i in range(1,len(s)):
    tmp1,tmp2=s[:i],s[i:]
    cnt1=1
    cnt2=1
    for j in range(len(tmp1)): cnt1*=int(tmp1[j])
    for j in range(len(tmp2)): cnt2*=int(tmp2[j])
    if cnt1==cnt2: print("YES"); ans=1;break
if ans==0:print("NO")