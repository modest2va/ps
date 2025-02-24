import sys
cnt=1
while True:
    
    n0=int(sys.stdin.readline())
    if n0==0: break
    else:
        n1=n0*3
        if n1%2==0: n2=int (n1/2)
        else: n2= int ( (n1+1)/2)
        n3=3*n2
        n4= int (n3/9)
    if n1%2==1: print("%d. odd %d"%(cnt,n4))
    else: print("%d. even %d"%(cnt,n4))
    cnt+=1
