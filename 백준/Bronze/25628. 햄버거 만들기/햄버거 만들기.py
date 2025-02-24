def sol(a,b):
    answer=min(a//2,b)
    return answer

a,b=map(int, input().split())
print(sol(a,b))