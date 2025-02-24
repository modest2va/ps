import sys
for _ in range(int(sys.stdin.readline())):
    dummy=sys.stdin.readline()
    tmp=list(map(int, sys.stdin.readline().split()))
    print(sum (tmp))