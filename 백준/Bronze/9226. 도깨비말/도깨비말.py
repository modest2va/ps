while True:
    s = input()
    if s == '#':
        break
    vowel = 'aeiou'
    if s[0] not in vowel:
        for i in range(len(s)):
            if s[i] in vowel:
                s = s[i:] + s[:i]
                break
    print(s+'ay')

