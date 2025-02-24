s=input()
tmp=[]
for i in s:
    tmp.append(int(i))
flag_zero= (tmp.count(0)!=0)
flag_three= (sum(tmp)%3==0)
if flag_three and flag_zero:
    tmp=sorted(tmp, reverse=True)
    for i in tmp:
        print(i,end='')
else : print(-1)