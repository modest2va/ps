import sys
for _ in range(int(sys.stdin.readline())):
    s=sys.stdin.readline()
    if s[len(s)//2] == s[len(s)//2 -1]:  print("Do-it")
    else: print("Do-it-Not")
