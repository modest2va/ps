def sol(n):
    months = 7 * (n - 1) + 8
    if months % 12 == 0:
        month = 12
        year = 2024 + months // 12 - 1

    else:
        month = months % 12
        year = 2024 + months // 12

    return [year, month]

if __name__ == '__main__':
    n = int(input())
    print(*sol(n))