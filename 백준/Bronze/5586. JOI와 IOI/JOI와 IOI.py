import sys
s=sys.stdin.readline()
cnt1=0
cnt2=0
for i in range(len(s)-2):
    if s[i]=='J' and s[i+1]=='O' and s[i+2]=='I': cnt1+=1
    elif s[i] == 'I' and s[i + 1] == 'O' and s[i + 2] == 'I': cnt2 += 1
print(cnt1)
print(cnt2)