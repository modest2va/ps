n=int(input())
if n%10!=0: print(-1)
else :
    a=int (n/300)
    n%=300
    b=int (n/60)
    n%=60
    c=int(n/10)

    print("%d %d %d"%(a,b,c))