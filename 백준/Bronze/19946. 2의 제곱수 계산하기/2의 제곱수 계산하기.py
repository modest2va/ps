ans=2**64-int(input())
cnt=0
while ans!=1:
    ans//=2
    cnt+=1
print(64-cnt)