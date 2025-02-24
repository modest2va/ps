def cal(n):
    r,c=0,0
    for i in range(1, n):
        if n%i==0 and i<=n//i:
            r,c= i,n//i
    return r,c
def sol(s,r,c):
    answer=[]
    for i in range(c):
        tmp=''
        for j in range(r):
            tmp+=s[r*i+j]
        answer.append(tmp)
    answer_string=''
    for i in range(r):
        for j in range(c):
            answer_string+=answer[j][i]
    return answer_string
s=input()
r,c=cal(len(s))
print(sol(s,r,c))