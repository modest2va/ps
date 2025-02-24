def sol(n, s):
    n = int(n)
    print(s*n)
if __name__ == '__main__':
    for _ in range(int(input())):
        n, s= input().split()
        sol(n, s)