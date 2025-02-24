def sol(n):
    for i in range(1,n+1):
        print('*'*i)
if __name__ == '__main__':
    while True:
        n=int(input())
        if n ==0 :
            break
        sol(n)