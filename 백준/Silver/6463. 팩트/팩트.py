while 1:
    ans=1
    i=0
    try:
        n=int(input())
        while i!=n:
            i+=1
            ans*=i
        while 1:
            cnt=ans%10
            if cnt: break
            ans//=10
        print("%5d -> %d" %(n,cnt))
    except: break