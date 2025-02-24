def sol(cards_a , cards_b):
    win_a, win_b = 0, 0
    answer = 'D'
    for i in range(10):
        if cards_a[i] > cards_b[i]:
            win_a+=1
        elif cards_a[i] < cards_b[i]:
            win_b += 1
    if win_a > win_b:
        answer = 'A'
    elif win_a < win_b:
        answer = 'B'
    return answer

if __name__ == '__main__':
    cards_a = list(map(int, input().split()))
    cards_b = list(map(int, input().split()))
    print(sol(cards_a,cards_b))