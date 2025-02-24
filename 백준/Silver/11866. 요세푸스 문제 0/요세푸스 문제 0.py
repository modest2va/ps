from collections import deque
n, k =map(int,input().split())
nums=[i+1 for i in range(n)]
nums = deque(nums)
answer = []
while nums:
    for i in range(k-1):
        nums.append((nums.popleft()))
    answer.append(nums.popleft())
answer = map(str, answer)
print('<',end='')
print(', '.join(answer) , end='')
print('>',end='')