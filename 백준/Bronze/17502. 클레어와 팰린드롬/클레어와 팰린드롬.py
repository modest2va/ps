n = int(input())
s = list(input())
answer = ''
for i in range(n):
    if s[i].isalpha():
        s[-i -1] = s[i]
    else:
        if s[-i -1] == '?':
            s[i] = 'a'
            s[-i - 1] = 'a'
print(''.join(s))