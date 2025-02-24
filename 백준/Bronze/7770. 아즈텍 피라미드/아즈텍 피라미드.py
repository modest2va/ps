import sys
n=int(sys.stdin.readline())
h=0
block=0
while block<=n:
    block+=2*h**2+h*2+1
    h+=1

print(h-1)