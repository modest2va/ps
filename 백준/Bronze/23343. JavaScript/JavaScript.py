def sol(x, y):
    if x.isdigit() and y.isdigit():
        return int(x)-int(y)
    else:
        return 'NaN'

if __name__ == '__main__':
    x, y = map(str, input().split())
    print(sol(x, y))
