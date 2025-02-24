def sol(strings):
    answer = 0
    for i in strings:
        if '01' in i or 'OI' in i:
            answer += 1

    return answer


if __name__ == '__main__':
    n = int(input())
    strings = [input() for i in range(n)]
    print(sol(strings))
