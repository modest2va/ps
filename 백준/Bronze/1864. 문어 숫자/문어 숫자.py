import sys
while 1:
    s=sys.stdin.readline()
    ans = 0

    if s[0]=="#": exit()
    else:
        for i in range(len(s)-1):
           if s[i] == '-': tmp = 0
           elif s[i] == "\\": tmp = 1
           elif s[i] == '(': tmp = 2
           elif s[i] == '@': tmp = 3
           elif s[i] == '?': tmp = 4
           elif s[i] == '>': tmp = 5
           elif s[i] == '&': tmp = 6
           elif s[i] == '%': tmp = 7
           elif s[i] == '/': tmp = -1
           ans+=tmp*pow(8,len(s)-i-2)
    print(ans)


