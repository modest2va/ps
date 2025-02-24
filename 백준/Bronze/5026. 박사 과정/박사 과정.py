import sys
for _  in range(int(sys.stdin.readline())):
    s=sys.stdin.readline()
    if s[0]=='P':
        print("skipped")
    else:
        print(eval(s))