t = int(input())
# 테스트 케이스의 수
for i in range(t):
    k = int(input())
    n = int(input())
    #k가 층이구요, n이 호 입니다
    apartment = [[0] * (n + 1) for i in range(k + 1)]


    for i in range(n + 1):
        apartment[0][i] = i

    for i in range(1, k + 1):
        for j in range(1, n + 1):
            apartment[i][j] = apartment[i][j - 1] + apartment[i - 1][j]
    print(apartment[k][n])