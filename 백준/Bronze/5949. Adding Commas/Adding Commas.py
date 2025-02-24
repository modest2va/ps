def sol(s):
    answer = ''
    for i in range(-1, -len(s) - 1, -1):
        answer += s[i]
        if i % 3 == 0 and i != -len(s) :
            answer += ','

    return answer[::-1]


if __name__ == '__main__':
    s = input()
    print(sol(s))