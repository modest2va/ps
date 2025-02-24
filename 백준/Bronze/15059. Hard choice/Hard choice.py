a,b,c=map(int,input().split())
a1,b1,c1=map(int,input().split())
cnt=0
if a1>a: cnt+= a1-a
if b1>b: cnt+= b1-b
if c1>c: cnt+= c1-c
print(cnt)