def sol(a, b, c, m):
    current = 0
    work = 0
    for i in range(24):
        if current < 0:
            current = 0

        if current + a > m:
            current -= c

        else:
            current += a
            work += b
    return work


a, b, c, m = map(int, input().split())
print(sol(a, b, c, m))
