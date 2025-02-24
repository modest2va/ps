a,b,c,d=map(int, input().split())
if a==c or b== d:
    print(0)
else:
    print (min(abs(a-c),abs(d-b),a,b))