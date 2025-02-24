import sys
tmp=[]
for i in range(int(input())):
    tmp.append(int(sys.stdin.readline()))
tmp.sort(reverse=True)
for i in tmp:
    print(i)