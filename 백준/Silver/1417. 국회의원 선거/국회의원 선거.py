def solution(dasom, people):
    if len(people) == 0:
        return 0
    people.sort(reverse=True)
    answer = 0
    while dasom <= people[0]:
        dasom += 1
        people[0] -= 1
        answer += 1
        people.sort(reverse=True)

    return answer


n = int(input())
dasom = int(input())
people = [int(input()) for i in range(n - 1)]
print(solution(dasom, people))
