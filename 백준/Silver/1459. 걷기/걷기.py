x,y,w,s=map(int, input().split())
goW=(x+y)*w
goS=min(x,y)*s+(x+y-min(x,y)*2)*w
if (x+y)%2==0 :goSW=s*max(x,y)
else: goSW= s*(max(x,y) -1) +w
print(min(goW,goSW,goS))