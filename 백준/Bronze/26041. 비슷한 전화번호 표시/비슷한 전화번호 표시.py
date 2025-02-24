a = list(map(str, input().split()))
b = input()
answer = 0

for phone_number in a:
    if b != phone_number and phone_number.startswith(b):
        answer += 1
print(answer)
