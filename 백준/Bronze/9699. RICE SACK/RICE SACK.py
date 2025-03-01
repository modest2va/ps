def sol(menu_price, menu_order):
    answer = 0

    for order in menu_order:
        answer += menu_price[order - 1]

    return answer


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print( f"Case #{i + 1}: {max(map(int, input().split()))}")