import sys
while True:
    a,b,c= map(int, sys.stdin.readline().split())
    if a ==b and b==c and a==0: break
    if c-b==b-a: print("AP %d"%(c+c-b))
    elif c//b==b//a : print("GP %d"%(c*c/b))