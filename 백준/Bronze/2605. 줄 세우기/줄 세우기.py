def sol(n,nums):
    answer=[]
    for i in range(1,n+1):
        answer.insert(nums[i-1],i)
    return answer[::-1]
n=int(input())
nums=list(map(int, input().split()))
print(*sol(n,nums))