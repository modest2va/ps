def sol(scores):
    grades = {'A+': 4.5,
              'A0': 4.0,
              'B+': 3.5,
              'B0': 3.0,
              'C+': 2.5,
              'C0': 2.0,
              'D+': 1.5,
              'D0': 1.0,
              'F': 0.0}
    total_gpa = total_class = 0
    for score in scores:
        name, times, result = score
        times = float(times)
        if result == 'P':
            continue
        total_gpa += times * grades[result]
        total_class += times
    return total_gpa/total_class

if __name__ == '__main__':
    scores = [input().split() for i in range(20)]
    print(sol(scores))
