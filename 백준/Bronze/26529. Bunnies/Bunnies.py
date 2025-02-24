def solution(n):
    answer = [1, 1]
    for i in range(2, n + 1):
        answer.append(answer[-1] + answer[-2])
    return answer[n]


if __name__ == '__main__':

    t = int(input())
    for i in range(t):
        n = int(input())
        print(solution(n))
