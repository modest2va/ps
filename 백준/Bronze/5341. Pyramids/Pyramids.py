def sol(n):
    return int(n*(n+1)/2)

if __name__ == '__main__':
    while 1:
        n = int(input())
        if n == 0:
            break
        print(sol(n))