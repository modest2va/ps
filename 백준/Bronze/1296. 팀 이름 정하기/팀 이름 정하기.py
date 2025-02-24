mn,cnt,name=input(),-1,""
for i in sorted([input() for _ in range(int(input()))]):
    l,o,v,e=mn.count('L')+i.count('L'),mn.count('O')+i.count('O'),+mn.count('V')+i.count('V'),mn.count('E')+i.count('E')
    cal= ((l+o)*(l+v)*(l+e)*(v+o)*(e+o)*(v+e))%100
    if (cnt<cal): cnt,name=cal,i
print(name)