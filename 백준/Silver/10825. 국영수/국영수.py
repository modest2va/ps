n=int(input())
ans=[]
for i in range(n):
    name,kor,eng,mathScore=input().split()
    kor=int(kor)
    eng = int(eng)
    mathScore = int(mathScore)
    ans.append([name,kor,eng,mathScore])
ans=sorted(ans, key=lambda x: (-x[1],x[2],-x[3],x[0]) )
for i in range(n):
    print(ans[i][0])