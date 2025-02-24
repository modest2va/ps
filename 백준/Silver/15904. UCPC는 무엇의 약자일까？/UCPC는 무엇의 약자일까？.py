s=input()
mylist='UCPC'
cnt=0
for i in range(len(s)):
    if cnt==4: break
    else:
        if s[i]== mylist[cnt]: cnt+=1
if cnt==4: print("I love UCPC")
else: print("I hate UCPC")