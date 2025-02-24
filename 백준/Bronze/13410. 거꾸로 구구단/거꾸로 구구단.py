n, k = map(int, input().split())
gugudan = []
for i in range(1, k + 1):
    gugudan.append(int(str(n*i)[::-1]))
print(max(gugudan))