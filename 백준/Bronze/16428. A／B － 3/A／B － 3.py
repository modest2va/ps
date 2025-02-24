def sol(a, b):
    if b <=0:
        return -(a//(-b)), a%(-b)
    else:
        return a//b, a%b

if __name__ == '__main__':
    a, b =map(int,input().split())
    q ,r =sol(a,b)
    print(q)
    print(r)