ans=0
current=0
for i in input():
    if abs(ord(i)-65-current)>12: ans+=26-abs(ord(i)-65-current); current=ord(i)-65
    else: ans+=abs(ord(i)-65-current); current=ord(i)-65
print(ans)