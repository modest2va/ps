tmp1=list(map(int,input().split()))
tmp2=list(map(int,input().split()))
a=sum(tmp1)
b=sum(tmp2)
if a>b : print("Gunnar")
elif a==b: print("Tie")
else: print("Emma")