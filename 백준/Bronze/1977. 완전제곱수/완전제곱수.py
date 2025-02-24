from math import ceil, floor
m = int(input())
n = int(input())
answer = []
for i in range(ceil(m ** 0.5), floor(n ** 0.5) + 1):
    answer.append(i ** 2)
if answer:
    print(sum(answer))
    print(min(answer))
else:
    print(-1)