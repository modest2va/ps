def sol(nums):
    return max(nums)*len(nums) -sum(nums)

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    print(sol(nums))