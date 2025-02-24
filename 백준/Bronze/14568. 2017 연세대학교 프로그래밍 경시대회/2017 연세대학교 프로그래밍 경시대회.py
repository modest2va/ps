import sys
n=int(sys.stdin.readline())
cnt=0
for i in range(1,n//2):
    for j in range(1,n):
        if 2*i+2*j+2<=n: cnt+=1
print(cnt)