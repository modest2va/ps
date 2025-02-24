import sys
def isRAT(a):
    if  a[2]**2==a[1]**2+a[0]**2 : return 1
    else: return 0

for i in range(1,int(sys.stdin.readline())+1):
    a=sorted(map(int, sys.stdin.readline().split()))
    print("Scenario #%d:"%i)
    if isRAT(a)==1:
        print("yes",'\n')

    else:
        print("no",'\n')
