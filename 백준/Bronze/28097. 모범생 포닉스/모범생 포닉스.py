def solution(n, t):
    total = sum(t) + (n - 1) * 8
    day, hour = total // 24, total % 24
    return day, hour


if __name__ == '__main__':
    n = int(input())
    t = map(int, input().split())
    print(*solution(n, t))
