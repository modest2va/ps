a,b,c=map(int , input().split())
finalScore=0
n=int(input())
for i in range(n):
    teamScore=0
    for j in range(3):
        aCnt,bCnt,cCnt=map(int,input().split())
        teamScore+=aCnt*a+bCnt*b+c*cCnt
    finalScore=max(finalScore,teamScore)
print(finalScore)