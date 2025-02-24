import sys
myplain="abcdefghijklmnopqrstuvwxyz"
for _ in range(int(sys.stdin.readline())):
    mycnt=[0]*26
    s=sys.stdin.readline()
    for i in range(len(s)-1):
        if s[i] in myplain: mycnt [ord (s[i])-97]+=1
    checkmax=0
    for i in range(26):
        if mycnt[i]==max(mycnt):
            checkmax+=1
            ans=i
    if checkmax ==1 : print(myplain[ans])
    else : print("?")