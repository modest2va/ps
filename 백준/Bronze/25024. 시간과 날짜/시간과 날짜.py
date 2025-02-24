def sol1(a,b):
    if  (a>=0 and a<=23 ) and (b>=0 and b<=59) : ans1='Yes'
    else :  ans1='No'
    return ans1
def sol2(a,b):
    thirty_one = [1,3,5,7,8,10,12]
    thirty = [4, 6 ,9 ,11]
    twenty_nine = [2]
    if  (a in thirty_one) and (b>=1 and b<=31) : ans2='Yes'
    elif (a in thirty) and (b>=1 and b<=30) : ans2='Yes'
    elif (a in twenty_nine) and (b >= 1 and b <= 29):ans2 = 'Yes'
    else :  ans2='No'
    return ans2
for i in range(int(input())):
    a,b=map(int, input().split())
    print("%s %s"%(sol1(a,b),sol2(a,b)))