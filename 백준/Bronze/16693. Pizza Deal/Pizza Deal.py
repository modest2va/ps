import sys
import math
a1,p1=map(int, sys.stdin.readline().split())
r1,p2=map(int, sys.stdin.readline().split())
if a1/p1< r1**2*math.pi/p2: print("Whole pizza")
else: print("Slice of pizza")