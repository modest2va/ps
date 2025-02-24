def calculate_cycle_length(N):
    original_N = N
    cycle_length = 0

    while True:
        tens = N // 10  # 주어진 수의 십의 자리 숫자
        ones = N % 10   # 주어진 수의 일의 자리 숫자

        new_digit = (tens + ones) % 10  # 새로운 숫자 계산

        N = ones * 10 + new_digit  # 새로운 수 생성

        cycle_length += 1  # 사이클 길이 증가

        if N == original_N:  # 원래 수로 돌아오면 종료
            break

    return cycle_length

# 입력 받기
N = int(input())
cycle_length = calculate_cycle_length(N)

# 결과 출력
print(cycle_length)
