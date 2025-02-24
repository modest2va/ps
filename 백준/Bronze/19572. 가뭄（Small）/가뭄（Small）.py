import sys
d1,d2,d3=map(int,sys.stdin.readline().split())

if (d1+d2-d3)/2<=0 or (d1-d2+d3)/2 <=0 or (-d1+d2+d3)/2 <=0 :
    print (-1)
else:
    print(1)
    print ((d1+d2-d3)/2, (d1-d2+d3)/2, (-d1+d2+d3)/2)