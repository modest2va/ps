import sys
a,b=map(int, sys.stdin.readline().split())
s=sys.stdin.readline()
cnt=0
for i in range(len(s)-1):
    if s[i]==' ' or s[i]== 'A' or s[i]== 'D' or s[i]== 'G' or s[i]== 'J' or s[i]== 'M' or s[i]== 'P' or s[i]== 'T' or s[i]== 'W': cnt+=a
    elif s[i]=='B' or s[i]== 'E' or s[i]== 'H' or s[i]== 'K' or s[i]== 'N' or s[i]== 'Q' or s[i]== 'U' or s[i]== 'X': cnt+= a*2
    elif s[i]=='C' or s[i]== 'F' or s[i]== 'I' or s[i]== 'L' or s[i]== 'O' or s[i]== 'R' or s[i]== 'V' or s[i]== 'Y' : cnt+= a*3
    elif s[i]=='S' or s[i]== 'Z': cnt+= a*4
for i in range(1, len(s)-1):
    if (s[i]=='A' or s[i]== 'B' or s[i]== 'C') and (s[i-1]== 'A' or s[i-1]== 'B' or s[i-1]== 'C'): cnt+=b
    if (s[i] == 'D' or s[i] == 'E' or s[i] == 'F') and (s[i - 1] == 'D' or s[i - 1] == 'E' or s[i - 1] == 'F'): cnt += b
    if (s[i] == 'G' or s[i] == 'H' or s[i] == 'I') and (s[i - 1] == 'G' or s[i - 1] == 'H' or s[i - 1] == 'I'): cnt += b
    if (s[i]=='J' or s[i] == 'K' or s[i] == 'L') and (s[i-1]=='J' or s[i - 1] == 'K' or s[i - 1] == 'L'): cnt+=b
    if (s[i] == 'M' or s[i] == 'N' or s[i] == 'O') and (s[i - 1] == 'M' or s[i - 1] == 'N' or s[i - 1] == 'O'): cnt += b
    if (s[i] == 'P' or s[i] == 'Q' or s[i] == 'R' or s[i] == 'S') and (s[i - 1] == 'P' or s[i - 1] == 'Q' or s[i - 1] == 'R' or s[i - 1] == 'S'): cnt += b
    if (s[i] == 'T' or s[i] == 'U' or s[i] == 'V') and (s[i - 1] == 'T' or s[i - 1] == 'U' or s[i - 1] == 'V'): cnt += b
    if (s[i] == 'W' or s[i] == 'X' or s[i] == 'Y' or s[i] == 'Z') and (s[i - 1] == 'W' or s[i - 1] == 'X' or s[i - 1] == 'Y' or s[i - 1] == 'Z'): cnt += b
print(cnt)