tmp=[]
for i in range(9):
    tmp.append(int(input()))
for i in range(9):
    for j in range(i+1,9):
        if sum(tmp)-tmp[i]-tmp[j]==100:
            x,y=i,j
            break
tmp.pop(x)
tmp.pop(y-1)
for i in tmp:
    print(i)