import collections
tmp=collections.deque()
for i in range(1,int(input())+1):
    tmp.append(i)
ans=[]
while len(tmp)!=1:
    ans.append(tmp[0])
    tmp.popleft()
    tmp.append(tmp[0])
    tmp.popleft()
ans.append(tmp[0])
print(*ans)