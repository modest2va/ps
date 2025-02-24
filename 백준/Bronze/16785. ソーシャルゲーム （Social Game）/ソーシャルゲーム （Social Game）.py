a,b,c=map(int,input().split())
for i in range(1,c//a+2):
    if a*i+(i//7)*b>=c: print(i); break