n=input()
mysize=len(n)
tmp=''
for _ in range(mysize): tmp+='1'
if mysize==1 : print(1)
elif int(n) >=int(tmp): print(mysize)
else: print(mysize-1)