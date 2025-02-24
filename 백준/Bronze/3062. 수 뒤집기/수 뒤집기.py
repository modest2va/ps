n = int(input())
for i in range(n):
    s = input()
    answer = str(int(s) + int(s[::-1]))
    if answer == answer[::-1]:
        print('YES')
    else:
        print('NO')
