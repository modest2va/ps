def sol(s):
    table=str.maketrans('aeios', '43105')
    return s.translate(table)

if __name__ == '__main__':
    s = input()
    print(sol(s))
