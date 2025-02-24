n = int(input())
for i in range(n):
    life = input()
    life = life.replace(' ', '')
    life_score = 0

    for j in life:
        life_score += ord(j) - 64

    if life_score == 100:
        print('PERFECT LIFE')
    else:
        print(life_score)