n=int(input())
p=int(input())
answer=0
if n<5:
    answer = p
elif n>=5 and n<10:
    answer = p-500
elif n>=10 and n<15:
    answer = min(p-500,int(p*0.9))
elif n>=15 and n<20:
    answer = min(p-2000,int(p*0.9))
elif n>=20:
    answer = min(p-2000,int(p*0.75))
if answer<0:
    answer = 0
print(answer)