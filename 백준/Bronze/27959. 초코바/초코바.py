def sol(n, m):
    if n * 100 >= m:
        return 'Yes'
    else:
        return 'No'


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(sol(n, m))
