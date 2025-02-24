def sol(a, b, c):
    if a + b == c:
        return "correct!"
    else:
        return "wrong!"


if __name__ == '__main__':
    a, b, c = map(int, input().split())
    print(sol(a, b, c))
