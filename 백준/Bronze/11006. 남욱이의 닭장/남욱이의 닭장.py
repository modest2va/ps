import sys
for _ in range(int(sys.stdin.readline())):
    a,b=map(int, sys.stdin.readline().split())
    print(b*2-a, b-(b*2-a))