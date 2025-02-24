n=int(input())
flag=n%2
s1=str(input())
s2=str(input())
if flag ==0:
    if s1!=s2 : print("Deletion failed")
    else: print("Deletion succeeded")
else:
    tmp=''
    for i in s1:
        if i=='1' : tmp+='0'
        else : tmp+='1'
    if tmp!=s2:        print("Deletion failed")
    else: print("Deletion succeeded")