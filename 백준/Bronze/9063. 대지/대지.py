def sol(xs, ys):
    if len(list(set(xs))) == 1 or len(list(set(ys))) == 1:
        return 0
    else:
        return (max(xs) - min(xs)) * (max(ys) - min(ys))


if __name__ == '__main__':
    n = int(input())
    xs = []
    ys = []
    for i in range(n):
        x, y = map(int, input().split())
        xs.append(x)
        ys.append(y)
    print(sol(xs, ys))