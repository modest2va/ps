n=int(input())
if n%2==0: print('a'*n)
else:
    if n==1: print('a')
    else: print('a'*(n//2)+'b'+'a'*(n//2))