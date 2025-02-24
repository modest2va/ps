a,b,c,d=map(int,input().split())
print(abs( a+b+c+d-(max(a,b,c,d))*2-(min(a,b,c,d))*2))