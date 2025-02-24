while 1:
    a,b,c=input().split()
    if a=='#': break
    if int( b)>17 or int(c) >79: print("%s Senior"%a)
    else: print("%s Junior"%a)