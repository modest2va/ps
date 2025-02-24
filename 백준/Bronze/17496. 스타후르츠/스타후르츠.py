a,b,c,d=map(int,input().split())
if a%b==0: print( (a//b-1)*c*d )
else: print( (a//b)*c*d )