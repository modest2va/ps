from collections import deque
n=int(input())
tmp=deque([i+1 for i in range(n)])
while len(tmp)>1:
    tmp.popleft()
    tmpNum=tmp.popleft()
    tmp.append(tmpNum)
print(tmp[0])