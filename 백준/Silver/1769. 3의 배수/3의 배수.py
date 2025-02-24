def sol(s):
    cnt = 0
    while len(s) > 1:
        cnt += 1
        answer = 0
        for i in s:
            answer += int(i)

        s = str(answer)

    if int(s) % 3 == 0:
        return (cnt, 'YES')
    else:
        return (cnt, 'NO')


s = input()
ans1, ans2 = sol(s)
print(ans1)
print(ans2)