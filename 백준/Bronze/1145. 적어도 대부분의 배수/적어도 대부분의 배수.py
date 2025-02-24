a,b,c,d,e=map(int, input().split())
for i in range(1,1000000):
    cnt=0
    if i%a==0: cnt+=1
    if i % b == 0: cnt += 1
    if i % c == 0: cnt += 1
    if i % d == 0: cnt += 1
    if i % e == 0: cnt += 1
    if cnt>2: print(i); break