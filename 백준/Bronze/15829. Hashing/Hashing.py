n=int(input())
s=input()
cnt=0
for i in range(n):
    cnt+=((ord (s[i])-96)*pow(31,i))
    cnt%=1234567891
print(cnt)