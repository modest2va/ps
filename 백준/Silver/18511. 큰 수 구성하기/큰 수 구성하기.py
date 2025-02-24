from itertools import product


def sol(n,k,nums):
    for i in range(len(str(n)),-1,-1):
        prod = list(product(nums, repeat=i))
        for j in prod:
            tmp=''.join(map(str,j))
            if n>=int(tmp):
                return (tmp)
n,k =map(int,input().split())
nums=sorted(list(map(int, input().split())) ,reverse=True)

print(sol(n,k,nums))