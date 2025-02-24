def sol(n):
    r = (n/3.141592)**(1/2)
    return 2*3.141592*r

if __name__ == '__main__':
    n = int(input())
    print(sol(n))