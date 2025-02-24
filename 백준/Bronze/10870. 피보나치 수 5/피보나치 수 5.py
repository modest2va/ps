def pibo(a):
    if a==0 :
        return 0
    if a==1:
        return 1

    return pibo(a-2)+pibo(a-1)

print (pibo(int(input())))