tmp=list(map(int,input().split()))

if not sum(tmp)<100: print("OK")
else:
    for i in range(len(tmp)):
        if tmp[i]==min(tmp):
            if i==0:print("Soongsil")
            if i == 1: print("Korea")
            if i == 2: print("Hanyang")