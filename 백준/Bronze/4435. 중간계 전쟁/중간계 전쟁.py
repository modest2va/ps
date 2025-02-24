def cal_gan(nums):
    score=0
    score_nums=[1,2,3,3,4,10]
    for i in range(len(nums)):
        score+=score_nums[i]*nums[i]
    return score

def cal_sauron(nums):
    score=0
    score_nums=[1,2,2,2,3,5,10]
    for i in range(len(nums)):
        score+=score_nums[i]*nums[i]
    return score
n=int(input())
for i in range(n):
    nums_gan = list(map(int,input().split()))
    nums_sauron = list(map(int, input().split()))
    ans=''
    if cal_gan(nums_gan) > cal_sauron(nums_sauron) :
        ans ='Good triumphs over Evil'
    elif cal_gan(nums_gan) < cal_sauron(nums_sauron) :
        ans ='Evil eradicates all trace of Good'
    else :
        ans = 'No victor on this battle field'
    print("Battle %d: %s"%(i+1, ans))