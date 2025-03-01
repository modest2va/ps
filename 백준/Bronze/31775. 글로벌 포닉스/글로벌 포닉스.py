def sol(string_list):
    is_start_l = 0
    is_start_k = 0
    is_start_p = 0
    for some_string in string_list:
        if some_string.startswith("l"):
            is_start_l = 1
        elif some_string.startswith("k"):
            is_start_k = 1
        elif some_string.startswith("p"):
            is_start_p = 1

    if is_start_l and is_start_k and is_start_p:
        return "GLOBAL"
    else:
        return "PONIX"


if __name__ == '__main__':
    string_list = [input() for i in range(3)]
    print(sol(string_list))
