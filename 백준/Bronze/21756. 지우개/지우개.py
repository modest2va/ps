n=int(input())
mylist=[i+1 for i in range(n)]
while len(mylist)>1:
    for i in range(0,len(mylist),2):
        mylist[i]=0
    while 0 in mylist:
        mylist.remove(0)
print(*mylist)