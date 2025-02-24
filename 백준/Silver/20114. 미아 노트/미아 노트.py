def sol(word):
    for i in word:
        if i != '?':
            return i
    return '?'

n, h, w = map(int, input().split())
alpha = [''] * n
for i in range(h):
    s = input()
    for j in range(0, len(s), w):
        alpha[j//w] += s[j:j + w]
answer = ''
for i in alpha:
    answer += sol(i)
print(answer)