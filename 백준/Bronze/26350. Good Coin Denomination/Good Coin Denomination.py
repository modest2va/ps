def sol(coins):
    flag = False
    for i in range(1,len(coins)):
        if 2*coins[i-1]>coins[i]:
            flag = True
            break
    print("Denominations:", *coins)
    if flag:
        print("Bad coin denominations!")
    else:
        print("Good coin denominations!")

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        nums = list(map(int, input().split()))[1:]
        sol(nums)
        if _!=n-1:
            print()
            