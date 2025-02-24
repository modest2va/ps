if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        a, b, x = map(int, input().split())
        w = (x - 1) * a + b
        print(w)
