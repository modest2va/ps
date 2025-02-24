def sol(s, d, i, l, n):
    stats = n * 4 - sum((s, d, i, l))
    if stats >= 0:
        return stats
    else:
        return 0


if __name__ == '__main__':
    s, d, i, l, n = map(int, input().split())
    print(sol(s, d, i, l, n))
