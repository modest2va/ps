import math
n=int(input())
if n%2==0  : print("I LOVE CBNU")
else:
    cnt= math.ceil(n/2)
    print("*"*n)
    print(" "*(cnt-1),end='')
    print("*")
    for i in range(1,cnt):
        print(" "*(cnt-i-1),end='')
        print("*",end='')
        print(" " * (2*i-1), end='')
        print("*",end='')
        print()

