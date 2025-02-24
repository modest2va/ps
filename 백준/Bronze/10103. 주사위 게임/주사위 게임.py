import sys
scoreChang=100
scoreSang=100
for _ in range(int(sys.stdin.readline())):
    a,b=map(int,sys.stdin.readline().split())
    if a<b: scoreChang-=b
    if a > b: scoreSang -= a
print(scoreChang)
print(scoreSang)