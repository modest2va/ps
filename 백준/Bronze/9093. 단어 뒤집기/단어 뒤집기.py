t = int(input())
for i in range(t):
    s=list(map(str, input().split()))
    new=[]
    for i in s:
        new.append(i[::-1])
    print(' '.join(new))