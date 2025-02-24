tmp=sorted(list(map(int,input().split())))
if tmp[1]-tmp[0] == tmp[2] -tmp[1]: print(2*tmp[2]-tmp[1])
elif tmp[2]-tmp[1]> tmp[1]- tmp[0] : print( (2*tmp[2]+tmp[0])//3)
else: print( (2*tmp[0]+tmp[2])//3)