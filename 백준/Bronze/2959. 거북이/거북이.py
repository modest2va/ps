import sys
tmp=list (map(int, sys.stdin.readline().split()))
tmp.sort()
print(tmp[0]*tmp[2])