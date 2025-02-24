mymax=0
for i in range(int(input())):
    s=input()
    cnt=s.count('for')+s.count('while')
    mymax=max(cnt,mymax)
print(mymax)