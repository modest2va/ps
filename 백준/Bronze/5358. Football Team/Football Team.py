def sol(s):
    answer = ''
    for alphabet in s:
        if alphabet == 'i':
            answer+='e'
        elif alphabet == 'I':
            answer+='E'
        elif alphabet == 'E':
            answer += 'I'
        elif alphabet == 'e':
            answer += 'i'
        else:
            answer += alphabet
    return answer


if __name__ == '__main__':
    while 1:
        try:
            s = input()
            print(sol(s))
        except:
            break