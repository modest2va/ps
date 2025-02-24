tmp=sorted(map(int, input().split()))
if tmp[0]== tmp[1] and tmp[1]==tmp[2]: print(2)
elif tmp[0]**2+tmp[1]**2==tmp[2]**2: print(1)
else: print(0)