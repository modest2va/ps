def btoD(n):
    n=str(n)
    ans=0
    for i in range(len(n)):
        ans+=pow(2,len(n)-i-1)*int(n[i])
    return(ans)
a,b=map(int, input().split())
print( bin (btoD(a)+btoD(b)) [2:] )