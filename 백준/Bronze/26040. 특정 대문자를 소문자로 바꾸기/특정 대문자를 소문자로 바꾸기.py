def sol(s, list_s):
    for capital_letter in list_s:
        s = s.replace(capital_letter, capital_letter.lower())
    return s

if __name__ == '__main__':
    s = input()
    list_s = list(input().split())
    print(sol(s, list_s))