a,b,c=map(int,input().split())
ans= c-11+(b-11)*60+(a-11)*1440
if ans<0: print(-1)
else:    print(ans)