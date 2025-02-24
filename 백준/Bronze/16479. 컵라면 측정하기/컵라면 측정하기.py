import sys
k=int(sys.stdin.readline())
d1,d2= map(int,sys.stdin.readline().split())
ans =k ** 2 - (((d1 - d2) / 2) ** 2)
if ans%1==0: print(int (ans))
else : print(ans )