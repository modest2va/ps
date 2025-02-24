def sol(encryption, message ):
    answer = ""
    for char in message:
        is_upper = False
        if char.isupper() :
            is_upper = True
        if char == " ":
            answer += " "
            continue
        decoded_char = encryption[ord(char.lower()) - 97]

        if is_upper:
            answer += decoded_char.upper()
        else:
            answer += decoded_char

    return answer



if __name__ == '__main__':
    e = input()
    m = input()
    print(sol(e, m))
