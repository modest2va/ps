x=[]
y=[]
for _ in range(3):
    tmpx,tmpy=map(int,input().split())
    x.append(tmpx)
    y.append(tmpy)
print ("%d %d"%((2*( min(x)+max(x))-sum(x)) , 2*( min(y)+max(y))-sum(y)))