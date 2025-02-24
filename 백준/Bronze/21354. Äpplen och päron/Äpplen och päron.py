def sol(a, p):
    if 7*a>13*p:
        return 'Axel'
    elif 7*a<13*p:
        return 'Petra'
    else:
        return 'lika'

if __name__ == '__main__':
    a, p = map(int, input().split())
    print(sol(a, p))