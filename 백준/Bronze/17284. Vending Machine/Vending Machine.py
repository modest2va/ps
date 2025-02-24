import sys
cnt=5000
tmp=list(map(int, sys.stdin.readline().split()))
for i in range(len(tmp)):
    if tmp[i]==1: cnt-=500
    elif tmp[i] == 2: cnt -= 800
    elif tmp[i] == 3: cnt -= 1000
print(cnt)