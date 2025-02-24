ggung=['i','pa','te','ni','niti','a','ali','nego','no','ili']
tmp=list(input().split())
for i in  range (1,len( tmp)):
    if tmp[i] in ggung:
        tmp[i]=''
for i in tmp:
    if not i=='' :
        print(i[0].upper(),end='')