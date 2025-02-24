import sys
n=int(sys.stdin.readline())
if n==1: print("*")
else:
    print(" "*(n-1)+"*")
    for i in range(n -2):
        print (" "*(n-2-i)+"*"+" "*(2*i+1)+"*")
    print("*"*(2*n-1))
