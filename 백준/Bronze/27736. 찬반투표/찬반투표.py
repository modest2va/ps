from math import ceil
def sol(nums):
    if nums.count(0) >= ceil(len(nums)/2):
        return 'INVALID'
    elif sum(nums) <= 0:
        return 'REJECTED'
    else:
        return 'APPROVED'



if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    print(sol(nums))