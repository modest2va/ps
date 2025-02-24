n=int(input())
for  i in range(n):
    number=int(input())
    print("Case %d:"%(i+1))
    for j in range(1,number//2+1):
        if j<=6 and number-j<=6:
            print("(%d,%d)"%(j,number-j))