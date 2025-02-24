import sys
n=int(input())
nums=list(map(int, sys.stdin.readline().split()))
sumNums=sum(nums)
ans=0
for i in nums:
    sumNums-=i
    ans+=i*sumNums
    ans%=(10**9+7)
print(ans)