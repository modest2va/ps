def sol(a, d, k):
    if (k - a) % d == 0 and (k - a) // d >= 0:
        return (k - a) // d + 1
    else:
        return 'X'


if __name__ == '__main__':
    a, d, k = map(int, input().split())
    print(sol(a, d, k))
