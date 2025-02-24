def sol(n):
    if n%2 == 1:
        return n*3+1
    else:
        return n//2

if __name__ == '__main__':
    n = int(input())
    cnt = 0
    while n!=1:
        n = sol(n)
        cnt+=1
    print(cnt)
