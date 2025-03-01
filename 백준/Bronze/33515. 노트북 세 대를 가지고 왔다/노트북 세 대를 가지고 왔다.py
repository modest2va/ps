def sol(t1, t2):
    return min(t1, t2)

if __name__ == '__main__':
    t1, t2 = map(int, input().split())
    print(sol(t1, t2))