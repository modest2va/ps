def sol(s):
    if s == '"' or s == '""':
        return 'CE'
    elif s.startswith('"') and s.endswith('"'):
        return s.replace('"', '')
    else:
        return 'CE'


if __name__ == '__main__':
    s = input()
    print(sol(s))