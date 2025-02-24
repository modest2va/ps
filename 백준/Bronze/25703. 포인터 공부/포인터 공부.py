def sol(n):
    print('int a;')
    print('int *ptr = &a;')
    if n==2:
        print('int **ptr2 = &ptr;')
    elif n>=3:
        print('int **ptr2 = &ptr;')
        for i in range(3,n+1):
            star = '*'*i
            print('int %sptr%d = &ptr%d;'%(star,i,i-1))
if __name__ == '__main__':
    n= int(input())
    sol(n)