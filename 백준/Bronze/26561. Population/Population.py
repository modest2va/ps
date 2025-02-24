def sol(p, t):
    answer = p - int(t/7) + int(t/4)
    return answer

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        p, t = map(int, input().split())
        print(sol(p, t))
