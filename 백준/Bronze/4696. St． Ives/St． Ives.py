def sol(n):
    ans=0
    for i in range(5):
        ans += n**i
    return ans

while 1:
    n=float(input())
    if n==0 :
        break
    print("%.2f"%sol(n))