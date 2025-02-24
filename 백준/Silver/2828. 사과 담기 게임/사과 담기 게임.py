import sys
n,m= map(int, sys.stdin.readline().split())
j=int(sys.stdin.readline())
left=1
ans=0
for i in range(j):
    apple=int(sys.stdin.readline())
    if apple<left:
        ans+=left-apple
        left=apple
    elif apple > left+m -1:
        ans+= apple-(left+m-1)
        left=apple-m+1
print(ans)