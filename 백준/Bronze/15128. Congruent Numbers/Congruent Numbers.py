def sol(p1, q1, p2, q2):
    area =  p1*p2/q1/q2/2
    if area == int(area):
        return 1
    else:
        return 0

if __name__ == '__main__':
    p1, q1, p2, q2 = map(int, input().split())
    print(sol(p1, q1, p2, q2))