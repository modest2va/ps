import math
n,k=map(int, input().split())
bg12=0
b34=0
g34=0
b56=0
g56=0
for _ in range(n):
    s,y=map(int,input().split())
    if y==1 or y==2: bg12+=1
    elif s==0:
        if y==3 or y==4 : g34+=1
        elif y==5 or y==6 : g56+=1
    elif s==1:
        if y==3 or y==4 : b34+=1
        elif y==5 or y==6 : b56+=1

print(math.ceil(bg12/k)+math.ceil(b34/k)+math.ceil(b56/k)+math.ceil(g34/k)+math.ceil(g56/k))