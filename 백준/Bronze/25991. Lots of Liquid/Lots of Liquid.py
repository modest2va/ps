def sol(liquids):
    total = 0
    for i in liquids:
        total += i**3
    answer = total**(1.0/3.0)
    return answer

if __name__ == '__main__':
    n_liquids =int(input())
    liquids = list(map(float, input().split()))
    print(sol(liquids))