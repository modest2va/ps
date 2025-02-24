if __name__ == '__main__':
    n=int(input())
    for i in range(n):
        lt,wt,le,we=map(int,input().split())
        if lt*wt<le*we:
            print("Eurecom")
        elif lt*wt>le*we:
            print('TelecomParisTech')
        else:
            print('Tie')