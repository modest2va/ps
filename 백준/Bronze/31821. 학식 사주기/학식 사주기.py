def sol(menu_price, menu_order):
    answer = 0

    for order in menu_order:
        answer += menu_price[order - 1]

    return answer


if __name__ == '__main__':
    n = int(input())
    menu_price = [int(input()) for i in range(n)]

    m = int(input())
    menu_order = [int(input()) for i in range(m)]

    print(sol(menu_price, menu_order))
