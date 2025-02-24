answer = [0, 5]
n = int(input())
for i in range(2, n + 1):
    answer.append(3* (i+1) -2)
print(sum(answer)%45678)