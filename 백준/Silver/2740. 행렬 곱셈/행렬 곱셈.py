x=[]
y=[]
xa,xb=map(int, input().split())
for i in range(xa):
    x.append(list(map(int, input().split())))
ya,yb=map(int, input().split())
for i in range(ya):
    y.append(list(map(int, input().split())))
result=[]
for i in range(xa):
    result.append([0]*yb)
for i in range(len(x)):
   for j in range(len(y[0])):
       for k in range(len(y)):
           result[i][j] += x[i][k] * y[k][j]
for r in result:
   print(*r) 