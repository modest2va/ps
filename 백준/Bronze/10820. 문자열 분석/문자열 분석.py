import sys
while True:

        s=sys.stdin.readline()
        a=0;b=0;c=0;d=0
        for i in range(len(s)-1):
            if ord(s[i])==32: d+=1
            elif ord(s[i])>= 48 and ord(s[i])<=57: c+=1
            elif ord(s[i])>= 65 and ord(s[i])<=91: b+=1
            elif ord(s[i]) >= 97 and ord(s[i]) <= 123: a+=1
        if a==0 and b==0 and c==0 and d==0:break
        print(a,b,c,d)
