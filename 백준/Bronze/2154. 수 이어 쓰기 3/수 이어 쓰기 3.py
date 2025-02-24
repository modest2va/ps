def sol(n):
    s = ''
    for i in range(1, n + 1):
        s += str(i)
    return s.find(str(n)) + 1

n = int(input())
print(sol(n))