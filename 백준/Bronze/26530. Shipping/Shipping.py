if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        x = int(input())
        total_price = 0
        for __ in range(x):
            name, unit, price = input().split()
            total_price += int(unit)*float(price)
        print('$%.2f'%(total_price))
        