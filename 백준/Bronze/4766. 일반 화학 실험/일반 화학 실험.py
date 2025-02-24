import sys
tmp=float(sys.stdin.readline())
while True:
    n=float(sys.stdin.readline())
    if int (n)==999: break
    print("%.2f"%(n-tmp))
    tmp=n