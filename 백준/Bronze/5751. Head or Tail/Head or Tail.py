while 1:
    n=int(input())
    if n==0: break
    tmp=list(map(int, input().split()))
    mary=tmp.count(0)
    john=tmp.count(1)
    print("Mary won %d times and John won %d times"%(mary,john))