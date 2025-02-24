from math import floor

scores={'A+': 4.3, 'A0': 4.0, 'A-': 3.7,
       'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
       'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
       'D+': 1.3, 'D0': 1.0, 'D-': 0.7,
       'F': 0.0}
n=int(input())
ans=0
sumScore=0
for i in range(n):
    name,score,grade=input().split()
    sumScore+=int(score)
    ans+=int(score)*scores[grade]
tmpScore=(ans/sumScore)*1000
if tmpScore%10>4:
    tmpScore=tmpScore+10-tmpScore%10
else:  tmpScore-=tmpScore%10
tmpScore/=1000
print("%.2f"%tmpScore)