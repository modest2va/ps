# 9개의 자연수를 저장할 리스트 생성
numbers = []

# 9개의 자연수를 입력받아 리스트에 추가
for i in range(9):
    num = int(input())
    numbers.append(num)

# 최댓값과 해당 값의 인덱스 찾기
max_value = max(numbers)
max_index = numbers.index(max_value)

# 최댓값 출력
print(max_value)

# 최댓값의 인덱스 출력 (인덱스는 0부터 시작하므로 +1)
print(max_index + 1)
