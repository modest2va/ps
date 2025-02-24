def sol(strings):
    answer = ''
    for i in range(15):
        for s in strings:
            if s:
                answer += s[0]
                s.pop(0)
            else:
                continue
    return answer


if __name__ == '__main__':
    strings = [list(input()) for i in range(5)]
    print(sol(strings))
