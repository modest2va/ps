def sol(s):
    s = s.lower()
    alpha = [0] * 26
    for i in s:
        if i.isalpha():
            alpha[ord(i) - 97] += 1

    if min(alpha) >= 3:
        return 'Triple pangram!!!'
    elif min(alpha) >= 2:
        return 'Double pangram!!'
    elif min(alpha) >= 1:
        return 'Pangram!'
    else:
        return 'Not a pangram'


t = int(input())
for i in range(t):
    s = input()
    print(f'Case {i + 1}: {sol(s)}')
