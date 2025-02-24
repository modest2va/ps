while 1:
    cnt=0
    try:
        a,b=map(int, input().split())
        for i in range(a,b+1):
            tmp=['0','1','2','3','4','5','6','7','8','9']
            tmp2=[0]*10
            i=str(i)
            for j in i:
                tmp2[int(j)]+=1
            flagDuplicate=0
            for j in tmp2:
                if j>1:flagDuplicate=1
            if flagDuplicate==0 : cnt+=1
        print(cnt)
    except :
        break