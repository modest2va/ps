def sol(l,k,score,problems,is_hard):
    if is_hard==1:
        plus_score=140
        location=1
    else:
        plus_score=100
        location=0
    problems.sort(key= lambda x: x[location])
    while k>0:
        if l >= problems[0][location]:
            problems.pop(0)
            k-=1
            score+=plus_score
        else:
            break
    return [k,score,problems]
n,l,k=map(int, input().split())
score=0
problems=[]
for i in range(n):
    sub1,sub2=map(int,input().split())
    problems.append([sub1,sub2])
k,score,problems=sol(l,k,score,problems,1)
answer=sol(l,k,score,problems,0)[1]
print(answer)