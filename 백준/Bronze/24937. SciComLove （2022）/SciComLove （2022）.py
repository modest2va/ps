def sol(s,n):
    answer = s[n:] + s[:n]
    return answer
s='SciComLove'
n=int(input())%10

print(sol(s,n))