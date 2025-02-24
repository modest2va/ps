n=int(input())
score=[int (input()) for i in range(n)]
mydp=[]
if n!=1 and n!=2:
    mydp.append(score[0])
    mydp.append(score[0]+score[1])
    mydp.append(max(score[0]+score[2],score[1]+score[2]))
    for i in range(3,n):
        mydp.append(max(mydp[i-2]+score[i],mydp[i-3]+ score[i]+score[i-1]))
    print(mydp[-1])
if n==1:
    print(score[0])
if n==2:
    print(score[0]+score[1])