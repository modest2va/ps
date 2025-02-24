def sol(a_nums,b_nums):
    a_len, a_nums = a_nums[0], a_nums[1:]
    b_len, b_nums = b_nums[0], b_nums[1:]
    a_nums.sort(reverse=True)
    b_nums.sort(reverse=True)
    if a_nums==b_nums:
        return 'D'
    for i in range(min(a_len, b_len)):
        if a_nums[i] > b_nums[i]:
            return 'A'
        elif a_nums[i] < b_nums[i]:
            return 'B'
        else:
            pass
    if a_len > b_len:
        return 'A'
    else:
        return 'B'

n=int(input())
for i in range(n):
    a_nums = list(map(int, input().split()))
    b_nums = list(map(int, input().split()))

    print(sol(a_nums,b_nums))
