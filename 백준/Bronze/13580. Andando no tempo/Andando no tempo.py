def sol(nums):
    nums.sort()
    if max(nums) ==  sum(nums) - max(nums):
        return 'S'
    elif nums[1] == nums[2] or nums[0] == nums[1]:
        return 'S'
    return 'N'

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    print(sol(nums))