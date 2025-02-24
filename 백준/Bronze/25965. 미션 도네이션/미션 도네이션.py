if __name__ == '__main__':
    n=int(input())
    for i in range(n):
        m= int(input())
        missions=[]
        for j in range(m):
            K,D,A= map(int,input().split())
            missions.append([K,D,A])
        k,d,a = map(int,input().split())
        money= 0
        for i in missions:
            if k*i[0] -d*i[1]+a*i[2]>0:
                money+=k*i[0] -d*i[1]+a*i[2]
        print(money)