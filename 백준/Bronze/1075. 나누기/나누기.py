import sys
n=int (sys.stdin.readline())
t=int (sys.stdin.readline())
n= (n//100)*100
for i in range(100):
    if (n+i)%t==0: print("%.2d"%i) ; exit()