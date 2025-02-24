def sol(yy):
    last_number = int(yy[:-3:-1][::-1])
    if (int(yy) + 1) % last_number == 0:
        return 'Good'
    else:
        return 'Bye'



if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        yy = input()
        print(sol(yy))

