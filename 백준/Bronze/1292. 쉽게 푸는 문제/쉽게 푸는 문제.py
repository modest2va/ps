a, b = map(int ,input().split())
nums = []
for i in range(1, 100):
    for j in range(i):
        nums.append(i)
print(sum(nums[a - 1: b]))