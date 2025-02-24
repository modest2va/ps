nums=[]
n=int(input())
for _ in range (n):
    s = input()
    tmpNum=''
    for i in s:
        if i.isnumeric() :
            tmpNum+=str(i)
        if i.isalpha():
            if tmpNum=='':continue
            else:
                nums.append(int(tmpNum))
                tmpNum=''
    if tmpNum!='' : nums.append(int(tmpNum))
for i in sorted(nums):
    print(i)