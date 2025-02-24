for i in range(int(input())):
    tmp=list(map(int,input().split()))
    listLen=tmp[0]
    tmp.pop(0)
    mymax=max(tmp)
    mymin=min(tmp)
    tmp=sorted(tmp)
    gap=0
    for j in range(1,len(tmp)):
        gap=max(tmp[j]-tmp[j-1],gap)
    print("Class %d"%(i+1))
    print("Max %d, Min %d, Largest gap %d"%(mymax,mymin,gap))