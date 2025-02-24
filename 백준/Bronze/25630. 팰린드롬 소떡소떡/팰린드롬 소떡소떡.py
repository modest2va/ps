n = int(input())
s = input()
answer = 0
for i in range(len(s)//2):
    if s[i] != s[-(i+1)]:
        answer += 1

print(answer)
