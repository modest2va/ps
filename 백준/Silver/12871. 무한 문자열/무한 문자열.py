# def gcd(x,y):
#     while (y) : x,y=y, x%y
#     return x
s=input()
t=input()
lenS=len(s)
lenT=len(t)
s=s*lenT
t=t*lenS
if s==t : print(1)
else : print(0)