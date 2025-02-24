import sys
a=int(sys.stdin.readline())
o=sys.stdin.readline()
b=int(sys.stdin.readline())

if o[0]=='*': print(a*b)
else: print(a+b)