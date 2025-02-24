for _ in range(int(input())):
    a,b=map(str, input().split())
    ans=int(str(a)[::-1])+int(str(b)[::-1])
    while ans%10 ==0:
        ans=ans/10
        ans=int(ans)
    print(str(ans)[::-1])
