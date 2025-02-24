import sys
def tmodecimal(tmp, b):
    ans=''
    while tmp>=b:
        ans+=str(tmp%b)
        tmp//=b
    ans+=str(tmp)
    return ans[::-1]
while 1:
    n=input()
    if n=='0': break
    b,tmp1,tmp2=n.split()
    tmp1=int(tmp1,int(b))
    tmp2 = int(tmp2, int(b))
    print(tmodecimal(tmp1%tmp2,int(b)))