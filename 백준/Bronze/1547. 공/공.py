# 컵의 개수 및 초기 공의 위치 설정
num_cups = 3
ball_position = 1

# 입력받을 위치 바꾸기 횟수
M = int(input())

# 위치 바꾸기 명령 실행
for _ in range(M):
    X, Y = map(int, input().split())
    if ball_position == X:
        ball_position = Y
    elif ball_position == Y:
        ball_position = X

# 결과 출력
print(ball_position)
