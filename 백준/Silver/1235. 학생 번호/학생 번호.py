n=int(input())
studentList=[input() for i in range(n)]
numberLen=len(studentList[0])
# print(studentList)
# print(numberLen)
for i in range(1,numberLen+1):
    compareList=[]
    for j in range(n):
        if studentList[j][numberLen-i:numberLen] in compareList: break
        else:
            compareList.append(studentList[j][numberLen-i:numberLen])
    #print(compareList)
    if len(compareList)==n:
        print(i)
        break
