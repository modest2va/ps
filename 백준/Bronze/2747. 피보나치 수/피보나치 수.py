import sys
fibotmp=[0]*100
def fibo(n):
    if n<=2:
        return 1
    if fibotmp[n]!=0: return fibotmp[n]
    else:
     fibotmp[n]=fibo(n-1)+fibo(n-2)
     return fibotmp[n]

print(fibo(int(sys.stdin.readline())))