import sys
for _ in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().split())
    if n<=11 or m<4 : print(-1)
    else : print(11*m+4)