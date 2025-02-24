import sys
a,b = sys.stdin.readline().split()
tmpA=[]
tmpB=[]
tmp=0

for i in range(len(a)):
     tmpA.append( int (a[i]))
for i in range(len(b)):
     tmpB.append( int (b[i]))

for i in range(len(tmpA)):
    for j in range(len(tmpB)):
        tmp+= tmpA[i]*tmpB[j]
print(tmp)

