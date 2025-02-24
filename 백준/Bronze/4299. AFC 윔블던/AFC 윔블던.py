import sys
a,b=map(int, sys.stdin.readline().split())
if (a+b)%2==1 or b>a: print(-1)
else: print( (a+b)//2, (a-b)//2  )