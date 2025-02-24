def sol(s, i, j):
    i,j = int(i), int(j)
    answer = s[:i]+s[j:]
    return answer
if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        s, i, j = input().split()
        print(sol(s, i, j))