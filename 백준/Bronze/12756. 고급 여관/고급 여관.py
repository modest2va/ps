import sys
import math
a,b=map(int,sys.stdin.readline().split())
c,d=map(int, sys.stdin.readline().split())
cnta=math.ceil(b/c)
cntb=math.ceil(d/a)

if cnta>cntb: print("PLAYER A")
elif cnta<cntb: print("PLAYER B")
elif cnta==cntb: print("DRAW")