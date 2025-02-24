import sys
n = int(sys.stdin.readline())
ans=0
for i in range(n):
    tmp=int(sys.stdin.readline())
    ans+=tmp
print(ans- (n-1))