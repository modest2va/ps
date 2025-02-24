import sys
s1,s2=map(int,sys.stdin.readline().split())
score1=0
score2=0
for i in range(s1):
    a,b=sys.stdin.readline().split()
    if a==b : score1+=1
for i in range(s2):
    a, b = sys.stdin.readline().split()
    if a == b: score2 += 1

if score1==s1 and score2==s2:print("Accepted")
elif score1!=s1 :print("Wrong Answer")
elif score1==s1 and (score2!=s2) : print("Why Wrong!!!")