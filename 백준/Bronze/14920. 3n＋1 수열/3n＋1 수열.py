import sys
c=[]
c.append(int(sys.stdin.readline()))

for i in range(1000000):
    if c[i]==1: break
    if c[i]%2==0 :c.append( c[i]//2 )
    else: c.append( 3*c[i]+1  )
print(len(c))