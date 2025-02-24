def sol(t, s):
    if t>=12 and t<=16 and s == 0:
        return 320
    else:
        return 280


if __name__ == '__main__':
    t, s = map(int, input().split())
    print(sol(t, s))
