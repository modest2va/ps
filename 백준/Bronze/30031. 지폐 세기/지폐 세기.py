def sol(width, length):
    if length != 68:
        return 0
    else:
        if width == 136:
            return 1_000
        elif width == 142:
            return 5_000
        elif width == 148:
            return 10_000
        elif width == 154:
            return 50_000


if __name__ == '__main__':
    n = int(input())
    total = 0
    for i in range(n):
        width, length = map(int, input().split())
        total += (sol(width, length))
    print(total)
