def sol(names):
    for i in names:
        g_cnt=i.lower().count('g')
        b_cnt = i.lower().count('b')
        if g_cnt>b_cnt:
            answer='GOOD'
        elif g_cnt<b_cnt:
            answer='A BADDY'
        else:
            answer='NEUTRAL'
        print("%s is %s"%(i,answer))

n=int(input())
names=[input() for i in range(n)]
sol(names)