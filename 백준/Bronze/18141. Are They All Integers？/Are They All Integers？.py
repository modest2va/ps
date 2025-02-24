from itertools import permutations
def solution(nums):
    nums = list(permutations(nums,3))
    for num in nums:
        if (num[0] - num[1]) / num[2] != (num[0] - num[1]) // num[2]:
            return 'no'
    return 'yes'


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    print(solution(nums))
