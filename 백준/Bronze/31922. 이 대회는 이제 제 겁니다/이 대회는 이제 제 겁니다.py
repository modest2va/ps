def sol(a, p, c):
    return max(a + c, p)

if __name__ == '__main__':
    a, p, c = map(int, input().split())
    print(sol(a, p, c))