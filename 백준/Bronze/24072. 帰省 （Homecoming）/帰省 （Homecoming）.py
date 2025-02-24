def sol(a, b, c):
    if a <= c < b:
        return 1
    else:
        return 0
if __name__ == '__main__':
    a, b, c = map(int, input().split())
    print(sol(a, b, c))