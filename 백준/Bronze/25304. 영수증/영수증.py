x=int(input())
n=int(input())
total_price = 0
for i in range(n):
    a, b =map(int, input().split())
    total_price+= a*b
if x == total_price:
    print("Yes")
else:
    print("No")