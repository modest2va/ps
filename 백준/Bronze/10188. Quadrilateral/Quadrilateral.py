def sol(x, y):
    for _ in range(y):
        print('X'*x)

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        x, y = map(int, input().split())
        sol(x, y)
        if _ != n-1:
            print()