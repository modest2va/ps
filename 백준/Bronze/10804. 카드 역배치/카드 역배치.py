tmp=[i+1 for i in range(20)]
for i in range(10):
    a,b=map(int, input().split())
    a-=1
    b-=1
    tmp[a:b+1]=tmp[a:b+1][::-1]
print(*tmp)