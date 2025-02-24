def sol(n, m):
    for row in range(n):
        ans = [i+m*row+1 for i in range(m)]
        print(*ans)
if __name__ == '__main__':
    n, m =map(int, input().split())
    sol(n,m)
