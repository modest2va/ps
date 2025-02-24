import sys
n=int(sys.stdin.readline())
tmp=[]
for _ in range(n):
    tmp.append(int(sys.stdin.readline()))
leftmax=tmp[0]
rightmax=tmp[len(tmp)-1]
cntLeft=1
cntRight=1
for i in range(n):
    if tmp[i]>leftmax : leftmax=tmp[i]; cntLeft+=1
for i in range(n):
    if tmp[n-1-i]>rightmax : rightmax=tmp[n-1-i]; cntRight+=1
print(cntLeft)
print(cntRight)