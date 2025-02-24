n=int(input())
for i in range(n):
    num=int(input())
    nums=[]
    for j in range(1,num):
        if j >= num-j :
            break
        else:
            nums.append([j,num-j])
    if len(nums)==0:
        print("Pairs for %d:"%num)
    else:
        print("Pairs for %d: "%num, end='')
        for k in range(len(nums)):
            if len(nums)!=1 and k!=len(nums)-1:
                print(*nums[k],end=', ')
            else:
                print(*nums[k],end='')
        print()