n = int(input())
for _ in range(n):
    mars_math = input().split()
    answer = float(mars_math[0])
    for i in range(1, len(mars_math)):
        if mars_math[i] == '@':
            answer *= 3
        elif mars_math[i] == '%':
            answer += 5
        elif mars_math[i] == '#':
            answer -= 7

    print(f'{answer:.2f}')