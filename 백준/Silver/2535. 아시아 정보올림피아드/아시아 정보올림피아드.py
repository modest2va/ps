def sol(n,nums):
    nums.sort(key=lambda x: x[2],reverse=True)
    nations=[0]*n
    cnt=0
    for i in range(len(nums)):
        if cnt==3:
            break
        if nations[nums[i][0]]!=2:
            nations[nums[i][0]]+=1
            cnt+=1
            print(nums[i][0],nums[i][1])
    return nums
n=int(input())
nums=[ list(map(int, input().split())) for i in range(n)]

(sol(n,nums))