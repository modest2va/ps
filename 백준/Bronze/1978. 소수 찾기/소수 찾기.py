def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input())
nums = list(map(int, input().split()))
answer = 0
for i in nums:
    if is_prime(i) == True:
        answer += 1
print(answer)