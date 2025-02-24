import sys
tmp= list (map(int,sys.stdin.readline().split()))
cnt=0
a,b,c,=map(int,sys.stdin.readline().split())
for i in range(4):
    if tmp[i]==a: print(i+1); cnt =1;break;
if cnt==0: print(0)