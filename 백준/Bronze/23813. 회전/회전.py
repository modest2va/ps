def sol(s):
    ans=0
    for i in range(len(s)):
        ans+=int(s[1:]+s[0])
        s=s[1:]+s[0]
    print(ans)

s=str(input())

sol(s)