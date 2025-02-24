def sol(num1, num2, cnt):
    for _ in range(cnt):
        if num1>num2:
            num1 = int(num1/2)
        else:
            num2 = int(num2 / 2)
    return max(num1,num2),min(num1,num2)

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        num1, num2, cnt = map(int, input().split())
        print('Data set: %d %d %d'%(num1,num2,cnt))
        print(*sol(num1, num2, cnt))
        if _ !=n-1:
            print()