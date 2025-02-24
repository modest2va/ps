def solution(n, a, b):
    if a == b:
        return 'Anything'
    elif a < b:
        return 'Bus'
    else:
        return 'Subway'


if __name__ == '__main__':
    n, a, b = map(int, input().split())
    print(solution(n, a, b))
