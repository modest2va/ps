import math
a,b,c=map(int, input().split())
r=math.sqrt(b**2+c**2)
print(int(a*b/r),int(a*c/r))