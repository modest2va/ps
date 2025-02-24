r,c,zr,zc=map(int,input().split())
for i in range(r):
    s=input()
    converted_s=''
    for j in s:
        converted_s+=j*zc
    for k in range(zr):
        print(converted_s)