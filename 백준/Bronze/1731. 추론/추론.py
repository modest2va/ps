import sys
n=int(sys.stdin.readline())
tmp=[]
for _ in range(n):
    tmp.append(int(sys.stdin.readline()))
if (tmp[1]-tmp[0])== (tmp[2]-tmp[1]):  print( tmp[-1]+tmp[1]-tmp[0])
elif (tmp[1]%tmp[0])== (tmp[2]%tmp[1]):  print( tmp[-1]*tmp[1]//tmp[0])