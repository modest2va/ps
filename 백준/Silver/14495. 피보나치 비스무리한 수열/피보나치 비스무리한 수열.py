def sol(n):
    if n <= 3:
        return 1
    answer = [0] * (n + 1)
    answer[1] = 1
    answer[2] = 1
    answer[3] = 1

    for i in range(4, n + 1):
        answer[i] = answer[i - 1] + answer[i - 3]

    return answer[n]
n = int(input())
print(sol(n))