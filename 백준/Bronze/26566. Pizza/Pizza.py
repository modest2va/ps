def sol(a1, p1, r1, p2):
    pi = 3.141592
    slice = a1/p1
    whole = (pi*r1**2)/p2
    if slice > whole:
        return 'Slice of pizza'
    else:
        return 'Whole pizza'

if __name__ == '__main__':
    n =  int(input())
    for _ in range(n):
        a1, p1 = map(int,input().split())
        r1, p2 = map(int, input().split())
        print(sol(a1, p1, r1, p2))
