def sol(nums):
    return nums[0] * nums[1] - nums[2] * nums[3] * nums[4]


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    print(sol(nums))
