if __name__ == '__main__':
    first_price, second_price = map(int, (input().split()))
    n = int(input())
    for _ in range(n):
        kwh = int(input())
        total = min(1000, kwh)*first_price + max(kwh-1000,0)*second_price
        print(kwh, total)