first=int(input())
cnt=0
answer_list=[]
for i in range(1, first+1):
    second=i
    nums=[first,second]
    while nums[-2]-nums[-1]>=0:
        nums.append(nums[-2]-nums[-1])
    if len(nums)>cnt:
        answer_list=nums
        cnt=len(nums)
print(cnt)
print(*answer_list)