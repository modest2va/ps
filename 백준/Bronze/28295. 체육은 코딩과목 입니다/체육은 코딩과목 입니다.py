if __name__ == '__main__':
    answer= ['N','E','S','W']
    idx = 0
    for i in range(10):
        n = int(input())
        if n == 3:
            idx -=1
        else:
            idx += n

    if idx < 0:
        idx = -((idx*-1)% 4)
    else:
        idx %= 4
    print(answer[idx ])