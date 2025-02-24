import sys
t=int(sys.stdin.readline())

for _ in range (t):
    br=sys.stdin.readline()
    studentN=int(sys.stdin.readline())
    tmp=[]
    for i in range(studentN):
        tmp.append(int(sys.stdin.readline()))
    if sum(tmp)%studentN==0: print("YES")
    else : print("NO")