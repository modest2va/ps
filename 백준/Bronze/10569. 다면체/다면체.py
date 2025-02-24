import sys
for _ in range(int(sys.stdin.readline())):
    v,e=map(int, sys.stdin.readline().split())
    print(e-v+2)