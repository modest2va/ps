import sys
n=int(sys.stdin.readline())
cnt=0
for i in range(1,n//3):
    for j in range(1, n // 3):
        for k in range(1, n // 3):
            if 3*i+3*j+3*k==n: cnt+=1
print(cnt)