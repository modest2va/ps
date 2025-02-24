def sol(n):
    start_num = n
    while n>=100:
        print(n)
        n = n//10 - n%10
    print(n)
    if n % 11 == 0:
        print('The number %d is divisible by 11.'%(start_num))
    else:
        print('The number %d is not divisible by 11.' % (start_num))

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        sol(n)
        if _ != t-1:
            print()