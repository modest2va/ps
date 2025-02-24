if __name__ == '__main__':
    num_word = int(input())

    word_dict = {}
    cnt = 1
    #word_dict = [input() for i in range(n)]
    for i in range(num_word):
        word_dict[input()] = 1
    n = int(input())
    for i in range(1, n+1):
        not_exist = []
        while True:
            s = input()

            if s == "-1":
                break
            if s not in word_dict:
                not_exist.append(s)

        if not_exist:
            print(f"Email {i} is not spelled correctly.")
            for word in not_exist:
                print(word)
        else:
            print(f"Email {i} is spelled correctly.")
    print("End of Output")