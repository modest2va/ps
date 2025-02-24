def fib(n):
    f=[[0,1],[1,0]]
    for i in range(2,n):
        f.append([f[i-1][0] + f[i-1][1] ,f[i-1][0] ] )
    return  sum(f[-1])
def fibonacci(n) :
    f=[0,1,1]
    for i in range(3,n+1):
        f.append( f[i - 1] + f[i - 2]) # 코드2
    return f[n]
n=int(input())
print(fib(n),n-2)