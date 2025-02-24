t = int(input())
for i in range(t):
    card = input()
    answer = 0
    for j in range(len(card)):
        if j % 2 == 0:
            num = 2 * int(card[j])
            if num>=10:
                num = num//10 + num%10
        else:
            num = int(card[j])
        answer += num
    if answer % 10 == 0:
        print('T')
    else:
        print('F')