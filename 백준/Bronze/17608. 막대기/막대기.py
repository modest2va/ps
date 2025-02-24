import sys
n=int(sys.stdin.readline())
tmp=[]
for _ in range(n):
    tmp.append(int(sys.stdin.readline()))
mymax=tmp[n-1]
cnt=1
for i in range(n):
    if mymax<tmp[n-2-i] : cnt+=1 ; mymax=tmp[n-2-i]
print(cnt)