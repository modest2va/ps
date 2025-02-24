def sol(a, b):
    return 1


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a, b = map(int, input().split())
        print(sol(a, b))
