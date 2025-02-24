def sol(n):
    answer = int(n,2)
    return answer

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        print(sol(n))
