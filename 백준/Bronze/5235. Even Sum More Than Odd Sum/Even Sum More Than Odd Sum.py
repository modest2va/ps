import sys
for i in range(int(sys.stdin.readline())):
    tmp=list(map(int, sys.stdin.readline().split()))[1:]
    odd,even=0,0
    for c in tmp:
        if c%2==0: even+=c
        else: odd+=c
    if even> odd: print("EVEN")
    elif even==odd :print("TIE")
    else: print("ODD")