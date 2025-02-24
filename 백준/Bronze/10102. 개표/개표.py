import sys
n=int(sys.stdin.readline())
s=sys.stdin.readline()
cntA=0
cntB=0
for i in range(n):
    if s[i]=='A': cntA+=1
    elif s[i]=='B' : cntB+=1
if cntA>cntB: print("A")
elif cntA<cntB: print("B")
else : print("Tie")