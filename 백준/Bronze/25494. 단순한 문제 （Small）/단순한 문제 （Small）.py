t = int(input())
for i in range(t):
    a, b, c = map(int,input().split())
    answer = 0
    for x in range(1, a + 1):
        for y in range(1, b + 1):
            for z in range(1, c + 1):
                if x % y == y % z and y % z == z % x:
                    answer += 1
    print(answer)