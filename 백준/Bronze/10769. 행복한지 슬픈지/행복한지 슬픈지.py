def sol(s):
    count_happy = count_sad = 0
    count_happy = s.count(':-)')
    count_sad = s.count(':-(')

    if count_happy == count_sad and count_happy == 0:
        return 'none'
    elif count_happy > count_sad:
        return 'happy'
    elif count_happy < count_sad:
        return 'sad'
    elif count_happy == count_sad:
        return 'unsure'

s = input()
print(sol(s))