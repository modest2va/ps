import math
import sys
a,b=map(int,sys.stdin.readline().split())
print(math.factorial(a)//math.factorial(b)//math.factorial(a-b))