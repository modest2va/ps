def sol(t1, t2):
    if t1 > t2:
        return t2 + 24 - t1
    else:
        return t2 - t1

if __name__ == '__main__':
    t1 = int(input())
    t2 = int(input())
    print(sol(t1,t2))