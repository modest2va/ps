import sys
tmp=[]
n=int(sys.stdin.readline())
for i in range(n):
    tmpNum=int(sys.stdin.readline())
    if tmpNum==0: tmp.pop()
    else: tmp.append(tmpNum)
print(sum(tmp))