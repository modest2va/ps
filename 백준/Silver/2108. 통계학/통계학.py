import sys
from collections import Counter
tmp=[]
n=int(sys.stdin.readline())
for  i in range(n):
    tmp.append(int(sys.stdin.readline()))
tmp.sort()
print(  int (round (sum(tmp)/n,0)))
print(tmp[n//2])
f = Counter(tmp)

b = f.most_common()

if len(tmp) > 1:
    if b[0][1] == b[1][1]:
        print(b[1][0])
    else:
        print(b[0][0])
else:
    print(tmp[0])

print(tmp[-1]-tmp[0])