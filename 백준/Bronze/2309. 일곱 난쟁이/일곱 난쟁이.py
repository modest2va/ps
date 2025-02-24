mylist=[]
for _ in range(9):
    mylist.append(int (input()))
mysum=sum(mylist)
mylist.sort()
for i in range(9):
    for j in range(i+1,9):
        if mysum-mylist[i]-mylist[j]==100:
            for k in range(9):
                if k==i or k==j:continue
                else:
                    print(mylist[k])
            exit()