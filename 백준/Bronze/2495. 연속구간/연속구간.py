for i in range(3):
    s = input()
    answer_list = []
    current_number = s[0]
    continue_num = 1
    for j in range(1, len(s)):
        if current_number == s[j]:
            continue_num += 1
        else:
            current_number = s[j]
            continue_num = 1
        answer_list.append(continue_num)
    print(max(answer_list))