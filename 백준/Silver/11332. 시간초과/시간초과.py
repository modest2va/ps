import math
import sys
def myFactorial(n,t,l):
    start=t
    for i in range(1,n+1):
        start*=i
        if start>(10**8)*l : return False
    return True
def solution(oper,n,t,l):
    n,t,l=int(n),int(t),int(l)
    if oper=='O(N)':
        bigO=n*t
    elif oper=='O(2^N)':
        bigO=(2**n)*t
    elif oper == 'O(N^3)':
        bigO=(n**3)*t
    elif oper == 'O(N^2)':
        bigO = (n**2) * t
    elif oper == 'O(N!)':
        return myFactorial(n,t,l)
    if (10**8)*l<bigO:return False
    else: return True
n=int(input())
for _ in range(n):
    oper,n,t,l=sys.stdin.readline().split()
    if solution(oper,n,t,l) : print("May Pass.")
    else:print("TLE!")