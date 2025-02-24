for _ in range(int(input())):
    ans=0
    cnt=0
    for i in input():
        if i=='O' :cnt+=1; ans+=cnt
        else: cnt=0
    print(ans)