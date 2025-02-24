import math
n=int(input())
for i in range(n):
    if i !=0 : print()
    tmp=1
    number=int(input())
    cnt=math.ceil(math.sqrt(number))
    if number==1: print ("1 is a deficient number.")
    else:
        for j in range(2,cnt):
            if number%j==0:
                tmp+=j+ number//j
        if tmp<number:
            print("%d is a deficient number."%number)
        if tmp==number:
            print("%d is a perfect number."%number)
        if tmp>number:
            print("%d is an abundant number."%number)