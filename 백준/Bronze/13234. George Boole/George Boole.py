def sol(s):
    s = list(s.split())
    s[0]=s[0].capitalize()
    s[1] = s[1].lower()
    s[2] = s[2].capitalize()
    if eval(s[0]+' ' + s[1]+' ' + s[2]):
        return 'true'
    else:
        return 'false'
    return
if __name__ == '__main__':
    s = input()
    print(sol(s))
