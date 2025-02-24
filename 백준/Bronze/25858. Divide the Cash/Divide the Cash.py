if __name__ == '__main__':
    n_students, total_prize = map(int, input().split())
    n_problems = [int(input()) for i in range (n_students)]
    total_problem = sum(n_problems)
    problem_per_prize = total_prize/total_problem
    for i in n_problems:
        print(int(i*problem_per_prize))