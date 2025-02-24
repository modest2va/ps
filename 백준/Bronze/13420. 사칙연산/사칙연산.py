n = int(input())
for i in range(n):
    s = input().split('=')
    left, right = s[0], int(s[1])
    a,b,c = left.split()
    a = int(a)
    c = int(c)
    if b == '+':
        left_answer = a + c
    if b == '-':
        left_answer = a - c
    if b == '*':
        left_answer = a * c
    if b == '/':
        left_answer = a // c
    if left_answer == right:
        print('correct')
    else:
        print('wrong answer')