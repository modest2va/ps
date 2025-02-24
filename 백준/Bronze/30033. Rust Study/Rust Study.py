def solution(a, b):
    answer = 0
    for an, bn in zip(a,b):
        if an <= bn:
            answer += 1
    return answer


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solution(a, b))
