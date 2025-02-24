def solution(n):
    if n % 42 == 0:
        return 'PREMIADO'
    else:
        return 'TENTE NOVAMENTE'


if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0:
            break
        print(solution(n))