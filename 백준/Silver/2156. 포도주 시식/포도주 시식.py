n=int (input())
score=[]
for i in range(n):
    score.append(int(input()))
mydp=[0]
if n!=1 and n!=2:
    mydp.append(score[0])
    mydp.append(score[0]+score[1])
    for i in range(3,n+1):
        ex1=score[i-1]+mydp[i-2]
        ex2=score[i-1]+score[i-2]+mydp[i-3]
        ex3=mydp[i-1]
        mymax=max(ex1,ex2,ex3)
        mydp.append(mymax)
    print(mydp[n])
if n==1:
    print(score[0])
if n==2:
    print(score[0]+score[1])