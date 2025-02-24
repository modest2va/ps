x, y = map(str, input().split())
x = x[::-1]
y = y[::-1]
answer = int(x) + int(y)
answer = str(answer)[::-1]

print(int(answer))