import sys
n=int(sys.stdin.readline())
tmp=list (map(int, sys.stdin.readline().split()))
youn=0
mins=0
for i in range(n):
    if tmp[i]<30: youn+=10
    else : youn+= (tmp[i]//30 + 1)*10
    if tmp[i]<60: mins+=15
    else : mins+= (tmp[i]//60 + 1)*15

if youn> mins : print("M %d"%mins)
if youn== mins : print("Y M %d"%mins)
if youn< mins : print("Y %d"%youn)