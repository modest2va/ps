def sol(nums):
    cnt_odd = cnt_even = 0
    for num in nums:
        if num % 2 == 0:
            cnt_even += 1
        else:
            cnt_odd += 1

    if cnt_odd < cnt_even:
        print('Happy')
    else:
        print('Sad')


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    sol(nums)