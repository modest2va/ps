cnt = 1
while 1:
    s=input()
    if s=='Was it a cat I saw?': break
    else:
        for i in range(0,len(s),cnt+1):
            print(s[i],end='')
        cnt+=1
        print()