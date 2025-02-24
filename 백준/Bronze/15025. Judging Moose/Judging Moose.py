a,b=map(int,input().split())
if a==b:
    if a==0 : print("Not a moose")
    else : print("Even %d"%(2*max(a,b)) )
else:print("Odd %d"%(2*max(a,b)) )