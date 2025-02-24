def perfect(n):
    n=int(n)
    divide=[]
    for i in range(1,n//2+1):
        if n%i==0 : divide.append(i)

    if sum(divide)==n:
        print("%d ="%n,end='')
        for i in range(len(divide)):
            if i!=len(divide)-1:print(" %d "%divide[i],end='+')
            else : print(" %d"%divide[i])
    else : print("%d is NOT perfect."%n)
while 1:
    n=int(input())
    if n==-1 : break
    perfect(n)