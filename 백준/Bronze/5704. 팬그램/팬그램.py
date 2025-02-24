import sys

while True:
    tmp = [0] * 26
    try :
        s=sys.stdin.readline()
        if s=="*": exit()
        else:
            for i in range(len(s)-1):
                if ord(s[i])!=32 :
                    tmp[ord(s[i])-97]=1
            if sum(tmp) ==26: print("Y")
            else: print("N")
    except : exit()