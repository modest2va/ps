def cal(n):
    if bin(n)[2:].count('1') % 2:
        return 1
    else:
        return 0


def sol(n, bit):
    if cal(n) == bit:
        return 'Valid'
    else:
        return 'Corrupt'


if __name__ == '__main__':
    for _ in range(int(input())):
        n, bit = map(int, input().split())
        print(sol(n, bit))
