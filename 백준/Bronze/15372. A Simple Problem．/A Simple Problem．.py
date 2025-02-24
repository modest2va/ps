import sys
def sol(n):
    return n*n

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(sys.stdin.readline())
        print(sol(n))