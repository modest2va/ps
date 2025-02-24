def sol(n):
    t = [1] * 36
    for i in range(1, 36):
        tmp = 0
        for j in range(i):
            tmp += t[j] * t[i-(j+1)]
        t[i] = tmp
    return t[n]
n = int(input())
print(sol(n))