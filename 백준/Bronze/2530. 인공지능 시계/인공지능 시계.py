import sys
a,b,c=map(int,sys.stdin.readline().split())
s=int(sys.stdin.readline())
c+=s%60
if c>59: c-=60; b+=1
b+=s//60
if b>59: a+=b//60; b%=60
a+=b//60
if a>23: a%=24
print("%d %d %d"%(a,b,c))