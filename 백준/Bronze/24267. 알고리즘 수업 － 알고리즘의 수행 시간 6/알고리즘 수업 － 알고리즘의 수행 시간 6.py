from math import factorial
if __name__ == '__main__':
    cnt = 0
    n = int(input())
    # for i in range(1, n-1):
    #     for j in range(i+1,n):
    #         for k in range(j+1,n+1):
    #             cnt+=1
    if n>=3:
        print(int(factorial(n)/(factorial(n-3)*factorial(3))))
    else:
        print(0)
    print(3)

