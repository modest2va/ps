def gcd(a,b):
    while(b):
        a,b=b,a%b
    return a



for _ in range(int(input())):
    n, *a=map (int, input().split())
    cnt=0
    for i in range(0,n-1):
        for j in range(i+1,n):
            cnt+=gcd(a[i],a[j])
    print(cnt)

