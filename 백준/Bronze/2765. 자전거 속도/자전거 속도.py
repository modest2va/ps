import sys
pi=3.1415927
n=1
while True:
    a,b,c=map(float, sys.stdin.readline().split())
    if b ==0 : break
    distance=a/(5280*12) *pi*b
    mph=distance/c *3600
    print("Trip #%d: %.2f %.2f" %(n,distance,mph))
    n+=1