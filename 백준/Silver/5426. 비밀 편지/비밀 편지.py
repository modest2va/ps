import math
n=int(input())
for _ in range(n):
    tmp=""
    s=input()
    arrn=int(math.sqrt(len(s)))
    for i in range(arrn):
        for j in range(arrn):
            tmp+=s[arrn*(j+1)-(i+1)]
    print(tmp)