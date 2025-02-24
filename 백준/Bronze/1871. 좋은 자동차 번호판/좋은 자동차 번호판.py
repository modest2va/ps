import sys
for _ in range(int(sys.stdin.readline())):
    l,d=sys.stdin.readline().split('-')
    cnt= (ord (l[0])-65)*(26**2) + (ord(l[1])-65)*26+ord (l[2])-65
    d= int(d)
    if abs(cnt-d)>100: print("not nice")
    else: print("nice")