s=int(input())
mybin=''
while s!=0:
    mybin+= str(s%2)
    s//=2
ans=0
for i in range(len(mybin)):
    ans+= int (mybin[i])*pow(2,len(mybin)-1-i)
print(ans)