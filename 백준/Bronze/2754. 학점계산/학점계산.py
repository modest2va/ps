s = input()

if s == 'F':
    print(0.0)
else:
    if s[0] == 'A':
        score = 4.0
    elif s[0] == 'B':
        score = 3.0
    elif s[0] == 'C':
        score = 2.0
    elif s[0] == 'D':
        score = 1.0

    if s[1] == '+':
        score += 0.3
    elif s[1] == '-':
        score -= 0.3

    print(score)
