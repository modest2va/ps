def nine(n):
    ans=''
    while n>0:
        ans+=str(n%9)
        n=n//9
    return ans[::-1]
print(nine(int(input())))