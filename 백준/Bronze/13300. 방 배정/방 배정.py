import math
n,k=map(int, input().split())
boys=[0]*6
girls=[0]*6
for _ in range(n):
    s,y=map(int,input().split())
    if s==0: girls[y-1]+=1
    else:boys[y-1]+=1
cnt=0
for i in range(6):
    cnt+=int (math.ceil( boys[i]/k)) +int (math.ceil( girls[i]/k))
print(cnt)