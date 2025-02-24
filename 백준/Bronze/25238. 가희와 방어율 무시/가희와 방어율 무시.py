def sol(a,b):
    if a*(100-b)/100 >= 100:
        return False
    else: return True
a, b= map(int, input().split())
if sol(a,b) == True :
    print(1)
else :
    print(0)