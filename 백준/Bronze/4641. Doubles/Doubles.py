def sol(nums):
    answer=-1
    for i in nums:
        if i*2 in nums:
            answer+=1
    return answer
while 1:
    nums=list(map(int, input().split()))
    if nums==[-1]:
        break
    else:
        print(sol(nums))