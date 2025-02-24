import sys
import math
cnt=1
while True:
    a,b,c=map(int,sys.stdin.readline().split())
    if a==b and b==c and a==0: break
    elif (a>=c or b>=c) and c!=-1 : print("Triangle #%d"%cnt); print("Impossible.")
    elif a==-1: print("Triangle #%d"%cnt); print("a = %.3f"% (math.sqrt(pow(c,2)-pow(b,2))))
    elif b == -1:
        print("Triangle #%d" % cnt); print("b = %.3f" % (math.sqrt(pow(c, 2) - pow(a, 2))))
    elif c == -1:
        print("Triangle #%d" % cnt); print("c = %.3f" % (math.sqrt(pow(a, 2) + pow(b, 2))))
    cnt+=1
    print()