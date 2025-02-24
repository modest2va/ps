n, k = map(int, input().split())
nums = list(map(int, input().split(',')))

for i in range(k):
    new_nums = []
    for j in range(1, len(nums)):
        new_nums.append(nums[j]-nums[j-1])
    nums = new_nums
nums = list(map(str, nums))
print(','.join(nums))