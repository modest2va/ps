def first(s):
    vowel = 'aeiou'
    for i in s:
        if i in vowel:
            return True

    return False


def second(s):
    vowel = 'aeiou'
    cnt_vowel = 0
    cnt_con = 0
    for i in s:
        if i in vowel:
            cnt_vowel += 1
            cnt_con = 0
            if cnt_vowel >= 3:
                return False
        else:
            cnt_con += 1
            cnt_vowel = 0
            if cnt_con >= 3:
                return False
    return True


def third(s):
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            if s[i] == 'e' or s[i] == 'o':
                pass
            else:
                return False
    return True


while True:
    s = input()
    if s == 'end':
        break

    if first(s) and second(s) and third(s):
        print(f'<{s}> is acceptable.')
    else:
        print(f'<{s}> is not acceptable.')
