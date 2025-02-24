def sol(n):
    answer = (n//2+1)**2

    return answer

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(sol(n))