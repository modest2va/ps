N=int(input())
for i in range(N):
    h,w,n=map(int,input().split())
    if n%h==0:
        ans=h*100+int (n/h)
        print(ans)
    else :
        ans = (n%h)*100+int(n/h)+1
        print (ans)