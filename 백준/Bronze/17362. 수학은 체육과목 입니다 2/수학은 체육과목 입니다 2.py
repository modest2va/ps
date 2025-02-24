n=int(input())
if n<6:
    print(n)
else :
   if n%8==1: print(1)
   if n%8==0 or n%8== 2: print(2)
   if n%8==7 or n%8== 3: print(3)
   if n%8==6 or n%8== 4: print(4)
   if n%8==5: print(5)