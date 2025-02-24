def sol(p,n,nums):
    nums.sort()
    answer = 0
    for i in range(n):
        if p < 200:
            answer += 1
            p += nums[0]
            nums.pop(0)
        else:
            break
    return(answer)
p, n=map(int,input().split())
nums=list(map(int, input().split()))

print(sol(p,n,nums))