from itertools import combinations_with_replacement


def solution(n):
    eureka = [1, 3, 6]
    start = 4
    while n >= eureka[-1]:
        eureka.append(eureka[-1] + start)
        start += 1
    pro = list(combinations_with_replacement(eureka, 3))
    for i in pro:
        if sum(i) == n:
            return 1
    return 0


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(solution(n))
