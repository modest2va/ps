def sol(n,nums):
    end=0
    start = nums[0]
    for i in range(n-1):
        if nums[i]<nums[i+1]:
            pass
        else :
            end=max(end,nums[i]-start)
            start = nums[i+1]
    if nums[n-2]<nums[n-1]:
        end = max(end,nums[n-1]-start)
    return end

n=int(input())
nums=list(map(int,input().split()))

print(sol(n,nums))