def sol(n, s) -> str:
    if s[-1] == 'G':
        return s[:n - 1]
    else:
        return s + 'G'


if __name__ == '__main__':
    n = int(input())
    s = str(input())
    print(sol(n, s))
