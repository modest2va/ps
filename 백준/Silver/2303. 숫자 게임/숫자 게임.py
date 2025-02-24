from itertools import combinations

n=int(input())
answer=[]
for i in range(n):
    nums = list(map(int, input().split()))
    mymax=0
    for nums_com in (list(combinations(nums, 3))):
        if mymax<sum(nums_com)%10:
            mymax = sum(nums_com)%10
    answer.append([i+1,mymax])
answer.sort(key=lambda x:(-x[1],-x[0]))
print(answer[0][0])