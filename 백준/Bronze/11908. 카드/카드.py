import sys
dummy=sys.stdin.readline()
tmp=list(map(int, sys.stdin.readline().split()))
print(sum(tmp)-max(tmp))