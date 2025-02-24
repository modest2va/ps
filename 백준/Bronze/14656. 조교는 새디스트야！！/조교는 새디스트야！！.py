import sys
n=int(sys.stdin.readline())
tmp=list(map(int,sys.stdin.readline().split()))
cnt=0
for i in range(n):
    if tmp[i]!=i+1 : cnt+=1
print(cnt)