def sol(a, b):
    if a>b:
        return 1
    elif a == b:
        return 0
    else:
        return -1


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(sol(a, b))
