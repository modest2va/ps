def solution(n):
    answer = [-1] * (n + 1)
    answer[0] = 0

    for i in range(3, n + 1):
        if answer[i - 3] != -1:
            answer[i] = answer[i - 3] + 1

        if answer[i - 5] != -1:
            if answer[i] == -1:
                answer[i] = answer[i - 5] + 1
            else:
                answer[i] = min(answer[i], answer[i - 5] + 1)
    return answer[n]

n = int(input())
print(solution(n))