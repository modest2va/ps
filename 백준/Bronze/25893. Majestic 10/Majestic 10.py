def sol(nums):
    triple_cnt = 0
    for i in nums:
        if i>=10:
            triple_cnt +=1
    if triple_cnt ==3:
        return 'triple-double'
    elif triple_cnt ==2:
        return 'double-double'
    elif triple_cnt ==1:
        return 'double'
    else:
        return 'zilch'

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        nums = list(map(int,input().split()))
        print(*nums)
        print(sol(nums))
        if _ != n-1:
            print()
