mylist=[]
for i in range(10):
    a=int(input())
    mylist.append(a%42)
ans=list(set(mylist))
print(len(ans))