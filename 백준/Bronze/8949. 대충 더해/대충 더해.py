a, b = input().split()
a = a.zfill(max(len(a), len(b)))
b = b.zfill(max(len(a), len(b)))
answer = ''
for i in range(len(a)):
    answer += str(int(a[i]) + int(b[i]))

print(answer)