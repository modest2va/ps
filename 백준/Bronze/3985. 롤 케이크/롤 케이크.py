l=int(input())+1
nums=[0]*l
n=int(input())
expected_value=0
expected_index=0
for i in range(n):
    p, k = map(int,input().split())

    if (k-p) > expected_value:
        expected_index=i+1
        expected_value=k-p

    for j in range(p,k+1):
        if nums[j]== 0:
            nums[j]=i+1
counting_sort=[0]*(n+1)
for i in nums:
    if i==0:
        pass
    else:
        counting_sort[i]+=1

print(expected_index)
print(counting_sort.index(max(counting_sort)))