def sol(s,shift):
    answer = ''
    for i in s :
        if ord(i)-shift<65:
            answer += chr(ord(i) -shift + 26)
        else:
            answer += chr(ord(i) - shift)

    return answer

if __name__ == '__main__':
    s = input()
    print(sol(s,shift=3))