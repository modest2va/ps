tmp=[0]*10
n=input()
for i in n:
    if int(i)==6 or int(i)==9 : tmp[6]+=1
    else: tmp[int(i)]+=1
tmp[6]= (tmp[6]+1)//2
print(max(tmp))