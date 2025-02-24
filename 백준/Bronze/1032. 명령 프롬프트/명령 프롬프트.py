n = int(input())
start = list(input())

for i in range(n - 1):
    s = list(input())
    for j in range(len(s)):
        if start[j] != s[j]:
            start[j] = '?'
print(''.join(start))