import sys
n,m = map(int, sys.stdin.readline().split())
A=list(map(int,sys.stdin.readline().split()))
B=list(map(int,sys.stdin.readline().split()))
print(sum(A)-sum(B))