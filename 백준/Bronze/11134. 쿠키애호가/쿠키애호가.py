import sys
import math

for _ in range(int(sys.stdin.readline())):
    a,b= map(int,sys.stdin.readline().split())
    print( math.ceil( a/b))
