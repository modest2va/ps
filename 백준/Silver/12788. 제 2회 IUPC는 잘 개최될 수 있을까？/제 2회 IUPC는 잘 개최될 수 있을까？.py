n=int(input())
m,k=map(int, input().split())
cntPencil=m*k
ctpList=sorted( list(map(int,input().split())) ,reverse=True)
start=0
currentPencil=0
flag=0
for i in ctpList:
    currentPencil+=i
    start+=1
    if currentPencil>= cntPencil:
        print(start)
        flag=1
        break
if flag==0: print("STRESS")
