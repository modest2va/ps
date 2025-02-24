while True:
    s = input()
    if s == '#':
        break
    s = s.lower()
    vowel = 'aeiou'
    answer = 0

    for i in vowel:
        answer += s.count(i)
    print(answer)