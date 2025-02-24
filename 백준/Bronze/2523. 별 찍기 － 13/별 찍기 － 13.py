import sys
n=int(sys.stdin.readline())

for i in range(n):
    for j in range(i+1):print("*",end='')
    print()
for i in range(n-1):
    for j in range(n-i-1):print("*",end='')
    if i!=n-1: print()