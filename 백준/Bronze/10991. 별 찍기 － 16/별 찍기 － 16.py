import sys
n=int(sys.stdin.readline())
if n==1: print("*")
elif n==2: print(" *\n* *")
else:
    print(" "*(n-1)+"*")
    print(" "*(n-2)+"* *")
    for i in range(n-2):
        print (" "*(n-3-i)+"* "*(i+2)+"*")