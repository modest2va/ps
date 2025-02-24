n=int(input())
scores=list(map(int,input().split()))
x,y=map(int,input().split())
absolute=0
for i in scores:
    if i>=y: absolute+=1
print((n*x//100),absolute)