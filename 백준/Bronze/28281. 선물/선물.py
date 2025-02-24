def sol(socks, units):
    my_max = socks[0] + socks[1]
    for i in range(len(socks) - 1):
        if my_max > socks[i] + socks[i-1]:
            my_max = socks[i] + socks[i-1]

    return my_max * units


if __name__ == '__main__':
    n, units = map(int, input().split())
    socks = list(map(int, input().split()))
    print(sol(socks, units))
