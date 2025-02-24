def sol(num1,num2):
    if num1 > num2 :
        return num1+num2
    else :
        return abs(num1-num2)
num1,num2=map(int,input().split())
print(sol(num1,num2))