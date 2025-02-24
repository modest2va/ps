import sys

s=int (sys.stdin.readline())
ji="JKLABCDEFGHI"
gan="7890123456"
print(ji[(s-1)%12]+gan[(s-1)%10])
