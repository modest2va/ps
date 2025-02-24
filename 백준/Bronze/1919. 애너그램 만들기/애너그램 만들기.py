import sys
s1=sys.stdin.readline()
s2=sys.stdin.readline()
tmp=[0]*26
tmp1=[0]*26
cnt=0
for i in range(len (s1)-1):
   tmp[ ord (s1[i]) -97 ] +=1
for i in range(len (s2)-1):
   tmp1[ ord (s2[i]) -97 ] +=1
for i in range(26):
   cnt+=abs(tmp[i]-tmp1[i])
print(cnt)