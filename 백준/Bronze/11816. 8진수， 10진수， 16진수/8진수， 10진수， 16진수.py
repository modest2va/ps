s=str(input())
ans=0
if s[0]!='0': print(int(s))
else:
    if s[1]=='x':
        s=s[2:]
        alpha='abcdef'
        for i in range(len(s)):
            if s[i] in alpha:
                ans+=(ord (s[i])-87)*pow(16,len(s)-i-1)
            else:
                ans+=int(s[i])*pow(16,len(s)-i-1)
    else:
        s=s[1:]
        for i in range(len(s)):
            ans+= int(s[i])*pow(8,len(s)-i-1)
    print(ans)