def sol(p ,q):
    if p <= 50 and q<=10:
        return 'White'
    elif q > 30:
        return 'Red'
    else:
        return 'Yellow'

if __name__ == '__main__':
    p = int(input())
    q = int(input())
    print(sol(p, q))