def sol(n, nums):
    sum_nums = sum(nums)
    nums.sort()
    answer = 0
    for i in range(n):
        answer += (sum_nums-nums[i])*nums[i]
        sum_nums -= nums[i]
    return answer


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    print(sol(n, nums))
