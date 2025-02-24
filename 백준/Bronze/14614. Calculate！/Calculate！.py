def sol(a, b, c):
    if c%2 == 1:
        return a^b
    else:
        return a

if __name__ == '__main__':
    a, b, c = map(int, input().split())
    print(sol(a, b, c))
