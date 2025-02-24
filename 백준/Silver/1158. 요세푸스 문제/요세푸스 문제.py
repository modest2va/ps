n,k=map(int, input().split())
joesephus=list(range(1,n+1))
ans=[]
i=k-1
while 1:
    ans.append(joesephus.pop(i))
    if not joesephus: break
    i= (i+k-1)%len(joesephus)
print('<'+ ', '.join(map(str, ans))+'>')