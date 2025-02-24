def sol(s):
    ans = ''
    for i in s:
        if (ord(i) + 1) <= 90:
            ans += chr(ord(i) + 1)
        else:
            ans += chr(ord(i) + 1 - 26)
    return ans

n=int(input())
for i in range(n):
    print("String #%d"%(i+1))
    s=input()
    print(sol(s))
    if i!= n-1:
        print()