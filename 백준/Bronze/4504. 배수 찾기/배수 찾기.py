import sys
n=int(sys.stdin.readline())
while True:
    a=int(sys.stdin.readline())
    if a==0: break
    else:
        if a%n==0: print("%d is a multiple of %d."%(a,n))
        else: print("%d is NOT a multiple of %d."%(a,n))