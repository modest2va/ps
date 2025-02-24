import sys
s=sys.stdin.readline()
yabai=[1,0,0]
for i in  range(len(s)):
    if s[i]=='A':
        tmp=yabai[0]
        yabai[0]=yabai[1]
        yabai[1]=tmp
    elif s[i]=='B':
        tmp = yabai[1]
        yabai[1] = yabai[2]
        yabai[2] = tmp
    elif s[i]=='C':
        tmp = yabai[0]
        yabai[0] = yabai[2]
        yabai[2] = tmp
print (yabai.index(1)+1)