def sol(n, m):
    answer = 0
    for a in range(1, n):
        for b in range(a + 1, n):
            if (a ** 2 + b ** 2 + m) % (a*b) == 0:
                answer += 1
    return answer

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    print(sol(n, m))
