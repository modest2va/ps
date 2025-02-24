import sys
import math
def log2(x):
    return (math.log10(x) / math.log10(2) )
def isPower2(n):
    if (math.ceil(log2(n))== math.floor(log2(n))) : return 1
    else: return 0
for _ in range(int(sys.stdin.readline())):
    a=int(sys.stdin.readline())
    print( isPower2(a)  )