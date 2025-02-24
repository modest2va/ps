tmp=[]
for i in range(8):
    tmp.append( [i+1, int(input())])
tmp=sorted(tmp,key=lambda  x: x[1])
ans=0
idx=[]
for i in range(5):
    ans+=tmp[i+3][1]
    idx.append(tmp[i+3][0])
print(ans)
print (*sorted(idx))