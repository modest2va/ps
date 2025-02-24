def check(s1,s2):
    if abs(ord(s1) - ord(s2))==1:
        return True
    else:
        return False
def sol(n,s):
    cnt=1
    for i in range(1,n):
        if cnt==5:
            return True
        if check(s[i],s[i-1]):
            cnt += 1
        else :
            cnt = 1
    if cnt == 5:
        return True
    else :
        return False
n=int(input())
s=input()
if sol(n,s) :
    print("YES")
else :
    print("NO")