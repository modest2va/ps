from bisect import bisect_left, bisect_right
def sol(n, nums):
    start_num = max(nums)
    for target  in range(start_num, -1, -1):
        bigger = n - bisect_right(nums, target) + nums.count(target)
        lower = bisect_left(nums, target)+nums.count(target)
        if bigger >= target:
            return target

if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    print(sol(n,nums))
    # print(bisect_left(nums, target)+nums.count(target))
    # print(n - bisect_right(nums, target) + nums.count(target))