if __name__ == '__main__':
    target = input()
    answer = 0
    while True:

        try:
            s = input()
            answer += s.count(target)
        except:
            break

    print(answer)
