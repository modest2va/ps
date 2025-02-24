if __name__ == '__main__':
    cnt = 0
    while 1:
        try:
            s = input()
            cnt += 1
        except:
            print(cnt)
            break