n,b=map(int,input().split())
answer=[]
while n>0:
    answer.append(n%b)
    n//=b
answer=answer[::-1]
for i in answer:
    if i<10:
        print(i,end='')
    else:
        print(chr(i+55),end='')