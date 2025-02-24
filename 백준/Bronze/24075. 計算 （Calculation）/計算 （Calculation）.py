def sol(a, b):
    print(max(a + b, a - b))
    print(min(a+b,a-b))

if __name__ == '__main__':
    a, b = map(int, input().split())
    sol(a, b)