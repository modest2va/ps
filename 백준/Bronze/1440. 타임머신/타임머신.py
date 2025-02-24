from itertools import combinations, permutations
def sol(per):
    answer = 0
    for time in per:
        if 1 <= time[0] <= 12 and 0 <= time[1] <= 59 and 0 <= time[2] <= 59:
            answer += 1

    return answer


nums = list(map(int, input().split(':')))
per = list(permutations(nums, 3))

print(sol(per))