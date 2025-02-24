def sol(a, b, n, w):
    answer = []
    for x in range(1, n):
        if a*x + b*(n - x) == w:
            answer.append((x, n - x))
    if len(answer) == 1:
        return answer[0]
    else:
        return [-1]


a, b, n, w = map(int, input().split())
print(*sol(a, b, n, w))
