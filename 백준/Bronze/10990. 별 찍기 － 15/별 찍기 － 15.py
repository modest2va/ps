import sys
n=int(sys.stdin.readline())
if n==1: print("*")
elif n==2: print(" *\n* *")
else:
    print(" "*(n-1)+"*")
    for i in range(n-1):
        print(" "*(n-i-2) +"*"+" "*(2*i+1)+"*")