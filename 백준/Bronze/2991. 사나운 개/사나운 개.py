import sys
a,b,c,d= (map(int, sys.stdin.readline().split()))
p,m,n=(map(int, sys.stdin.readline().split()))
cntp=0;cntm=0;cntn=0
if (p%(a+b))<=a and p%(a+b)!=0: cntp+=1
if (p%(c+d))<=c and p%(c+d)!=0: cntp+=1
if (m%(a+b))<=a and m%(a+b)!=0: cntm+=1
if (m%(c+d))<=c and m%(c+d)!=0: cntm+=1
if (n%(a+b))<=a and n%(a+b)!=0: cntn+=1
if (n%(c+d))<=c and n%(c+d)!=0: cntn+=1
print(cntp)
print(cntm)
print(cntn)