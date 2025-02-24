def sol(s):
    alpha = [0] * 26
    check = False

    for i, v in enumerate(s):
        if check:
            check = False
            continue
        alpha[ord(v) - 65] += 1

        if alpha[ord(v) - 65] == 3:
            if i == len(s) - 1:
                return 'FAKE'
            elif s[i] != s[i + 1]:
                return 'FAKE'

            check = True
            alpha[ord(s[i]) - 65] = 0
    return 'OK'


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        print(sol(s))
