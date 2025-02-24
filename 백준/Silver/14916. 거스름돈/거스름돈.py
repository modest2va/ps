n=int(input())

if n<5:
    if n==1 or n==3: print(-1)
    else : print (int (n/2))
else:
    if n%5== 0: print(int (n/5))
    else:
        if (n%5)%2==1:
            print(n//5-1+int (((n%5)+5)/2))
        else : print(n//5+int ((n%5)/2))