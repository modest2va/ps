while 1:
    tmp=sorted(list(map(int, input().split())))
    if sum(tmp)==0 : break
    if (sum(tmp)-tmp[0]-tmp[5])/4 ==int ((sum(tmp)-tmp[0]-tmp[5])/4): print(int ((sum(tmp)-tmp[0]-tmp[5])/4))
    else: print((sum(tmp)-tmp[0]-tmp[5])/4)