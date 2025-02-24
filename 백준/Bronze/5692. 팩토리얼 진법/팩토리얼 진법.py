import math
import sys
while 1:
    n=sys.stdin.readline().rstrip()
    if n=='0' : break
    cnt=0
    for i in range(len(n)):
       cnt+= int(n[i])*math.factorial(len(n)-i)
    print(cnt)