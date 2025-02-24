n, p = map(int, input().split())
nums=[n]
while 1:
    if (nums[-1]*n)%p not in nums:
        nums.append((nums[-1]*n)%p)
    else:
        print(len(nums)-(nums.index((nums[-1]*n)%p)))
        break