n=int(input())
tmp=[]
for i in range(n):
    tmp.append(input())
tmpD=sorted(tmp,reverse=True)
tmpI=sorted(tmp)
if tmp== tmpD :print("DECREASING")
elif tmp ==tmpI:print("INCREASING")
else: print("NEITHER")