def sol(a, b, c):
    for x in range(a, 0, -1):
        for y in range(b, 0, -1):
            for z in range(c, 0, -1):
                if x + y + z - max(x, y, z) > max(x, y, z):
                    return x + y + z


if __name__ == '__main__':
    a, b, c = map(int, input().split())
    print(sol(a, b, c))
