def sol(n):
    man, gu, ggyu = 300, 275, 250
    if n >= man:
        return 1
    elif n >= gu:
        return 2
    elif n >= ggyu:
        return 3
    else:
        return 4


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    for i in nums:
        print(sol(i), end=' ')
