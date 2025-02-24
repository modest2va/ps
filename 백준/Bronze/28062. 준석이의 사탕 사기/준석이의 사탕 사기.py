def solution(nums):
    answer = 0
    odd_nums = []
    for num in nums:
        if num % 2 == 0:
            answer += num
        else:
            odd_nums.append(num)
    odd_nums.sort(reverse = True)
    answer += sum(odd_nums[:(len(odd_nums)//2)*2])

    return answer

n = int(input())
nums = list(map(int, input().split()))
print(solution(nums))