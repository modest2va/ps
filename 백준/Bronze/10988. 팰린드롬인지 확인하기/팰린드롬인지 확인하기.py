def sol(s):
    if s==s[::-1] :
        return 1
    else :
        return 0

s=input()
print(sol(s))