first,second,third=[],[],[]
n=int(input())
for i in range(n):
    a,b,c=map(int, input().split())
    first.append(a)
    second.append(b)
    third.append(c)
first = [sum(first), first.count(3), first.count(2), first.count(1),1]
second = [sum(second), second.count(3), second.count(2), second.count(1),2]
third = [sum(third), third.count(3), third.count(2), third.count(1),3]
answer=[first,second,third]
answer.sort(key= lambda x: (x[0],x[1],x[2]), reverse=True)

if answer[0][:4]==answer[1][:4]:
    print(0,answer[0][0])
else:
    print(answer[0][4],answer[0][0])
