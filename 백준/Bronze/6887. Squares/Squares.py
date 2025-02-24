def sol(n):
    return int(n**(1/2))

if __name__ == '__main__':
    n = int(input())
    print("The largest square has side length %d."%sol(n))