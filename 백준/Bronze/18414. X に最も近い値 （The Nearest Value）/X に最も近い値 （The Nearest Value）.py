a,b,c=map(int,input().split())
if b<=a and a<=c: print(a)
elif abs(c-a) >abs(b-a) :print(b)
else: print(c)