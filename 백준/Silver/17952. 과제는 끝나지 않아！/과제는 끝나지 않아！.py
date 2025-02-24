#17952
import sys
n=int(input())
assignmentList=[]
score=0
for i in range (n):
    task=list(map(int, sys.stdin.readline().split()))
    if task[0]==1:
        assignmentList.append([task[1],task[2]])
    if assignmentList:
        assignmentList[-1][1]-=1
        if assignmentList[-1][1]==0:
            score += assignmentList[-1][0]
            assignmentList.pop()
print(score)