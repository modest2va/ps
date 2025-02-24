def sol(s):
    pseudo_latin = {'a':'as',
                    'i':'ios',
                    'y':'ios',
                    'l':'les',
                    'n':'anes',
                    'ne':'anes',
                    'o':'os',
                    'r':'res',
                    't':'tas',
                    'u':'us',
                    'v':'ves',
                    'w':'was'}
    if s[-1] in pseudo_latin:
        s=s[:len(s)-1]+pseudo_latin[s[-1]]
    elif s[len(s)-2:] in pseudo_latin:
        s = s[:len(s)-2] + pseudo_latin[s[len(s)-2:]]
    else:
        s = s+'us'

    return s

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        s = input()
        print(sol(s))