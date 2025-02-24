stickList=list(map( int, input().split()))
cnt=0
for i in range(5):
    for j in range(i+1,5):
        for k in range(j + 1, 5):
            if stickList[i]+stickList[j]+stickList[k] >2*max(stickList[i],stickList[j],stickList[k]) :
                cnt+=1
print(cnt)