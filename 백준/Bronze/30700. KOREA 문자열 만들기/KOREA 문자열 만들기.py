def sol(s):
    korea = 'KOREA'
    current = 0
    answer = 0
    for alphabet in s:
        if alphabet == korea[current]:
            current = (current + 1) % 5
            answer += 1
    return answer

s = input()
print(sol(s))

