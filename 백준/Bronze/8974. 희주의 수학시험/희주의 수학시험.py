def make(n):
    tmp=[]
    for i in range(1,n+1):
        for j in range(i):
            tmp.append(i)
    return tmp

a,b=map(int,input().split())
print( sum (make(b)[:b])- sum(make(b)[:a-1]) )