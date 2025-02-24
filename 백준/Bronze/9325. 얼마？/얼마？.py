import sys
for i in range(int(sys.stdin.readline())):
    s=int(sys.stdin.readline())
    numberO=int(sys.stdin.readline())
    for j in range(numberO):
            a,b=map(int,sys.stdin.readline().split())
            s+=a*b
    print(s)