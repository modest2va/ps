def solution(n):
    answer = [0, 1, 1]
    for i in range(3, n + 1):
        answer.append(answer[-1] + answer[-2])
    return answer[n]


if __name__ == '__main__':
    while True:
        n = int(input())
        if n == -1:
            break
        print(f'Hour {n}: {solution(n)} cow(s) affected')
