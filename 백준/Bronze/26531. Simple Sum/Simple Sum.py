def sol(s):
    left,right = s.split('=')
    if eval(left) == int(right):
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    s = input()
    print(sol(s))
