import sys
n=int(sys.stdin.readline())
tmp=list(map(int, sys.stdin.readline().split()))
tmp.sort()
tmp.reverse()
for i in range(n):
    tmp[i]+=i+1
print(max(tmp)+1)