x,y=map(int,input().split())
for i in range(1, 10**10):
    cmpX,cmpY=i/x,i/y
    if cmpX>=1+cmpY:
        if (i%x) ==0 :print(i//x) ;break
        else : print(i//x+1) ; break