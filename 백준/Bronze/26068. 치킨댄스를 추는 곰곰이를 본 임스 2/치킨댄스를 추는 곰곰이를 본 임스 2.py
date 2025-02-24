if __name__ == '__main__':
    n =int(input())
    answer = 0
    for _ in range(n):
        gifticon = input()
        if int(gifticon[2:])<=90:
            answer+=1
    print(answer)