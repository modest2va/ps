import sys
a,b= map(int,sys.stdin.readline().split())
start= int ((1+a)*a/2)
for i in range(a+1,b+1):
    start*= int ( (i*(1+i))/2)
print(start%14579)