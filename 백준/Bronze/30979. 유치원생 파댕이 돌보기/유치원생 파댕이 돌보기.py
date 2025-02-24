def sol(t, candys):
    if t > candys:
        return "Padaeng_i Cry"
    else:
        return "Padaeng_i Happy"


if __name__ == '__main__':
    t = int(input())
    n = int(input())
    candys = sum(list(map(int, input().split())))
    print(sol(t, candys))
