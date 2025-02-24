def sol(s):
    if s.count('2')>s.count('e'):
        return 2
    elif s.count('2')<s.count('e'):
        return 'e'
    elif s.count('2')==s.count('e'):
        return 'yee'
    
if __name__ == '__main__':
    n = int(input())
    s = input()
    print(sol(s))
    