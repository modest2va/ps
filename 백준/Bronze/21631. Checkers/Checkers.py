def sol(a, b):
    if a>=b:
        return b
    else:
        return a+1

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(sol(a, b))