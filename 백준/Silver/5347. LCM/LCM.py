def gcd(a,b):
   if b==0 : return a
   else :return gcd(b,a%b)

n=int(input())
for _ in range(n):
   a,b=map(int,input().split())
   print(gcd(a,b)*a//gcd(a,b)*b//gcd(a,b))