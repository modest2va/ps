if __name__ == '__main__':
    a = int(input())
    w, v = map(int, input().split())
    if w / v >= a:
        print(1)
    else:
        print(0)
