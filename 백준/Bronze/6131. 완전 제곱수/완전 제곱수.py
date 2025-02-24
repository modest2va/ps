def sol(n):
    answer = 0
    for b in range(1, 501):
        for a in range(b, 501):
            if a**2 == b**2 + n:
                answer += 1

    return answer

n = int(input())
print(sol(n))
