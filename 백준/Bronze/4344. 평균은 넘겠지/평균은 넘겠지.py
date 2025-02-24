def calculate_percentage(scores):
    total_students = scores[0]
    student_scores = scores[1:]
    average = sum(student_scores) / total_students
    above_average = len([score for score in student_scores if score > average])
    percentage = (above_average / total_students) * 100
    return round(percentage, 3)


# 입력 처리 및 결과 출력
test_cases = int(input())
results = []

for _ in range(test_cases):
    scores = list(map(int, input().split()))
    results.append(calculate_percentage(scores))

for result in results:
    print(f"{result:.3f}%")
