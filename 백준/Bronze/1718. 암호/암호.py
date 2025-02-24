myPlain=input()
key=input()
b=len(key)
for i in range(len(myPlain)):
    if myPlain[i]==' ': print(" ",end='')
    else:
        if ord(myPlain[i])-ord(key[i%b])<=0:
            print(chr(ord(myPlain[i]) - ord(key[i%b]) +26+ 96), end='')
        else :print( chr(ord(myPlain[i])-ord(key[i%b])+96 ), end='' )