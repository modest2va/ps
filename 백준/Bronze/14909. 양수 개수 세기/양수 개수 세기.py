import sys
tmp=list(map(int, sys.stdin.readline().split()))
cnt=0
for i in range(len(tmp)):
    if tmp[i]>0: cnt+=1
print(cnt)