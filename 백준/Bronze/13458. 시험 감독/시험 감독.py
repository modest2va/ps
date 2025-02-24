import math
cnt=0
n=int(input())
ai=list(map(int, input().split()))
b,c=map(int, input().split())
for i in range(n):
    cnt+=1
    if ai[i]-b>0 :
        cnt+=math.ceil((ai[i]-b)/c)
print(cnt)