def sol(s):
    left, right = s.split('=')
    if eval(left)==int(right):
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        s = input()
        s = s.replace(' ','')
        print('Case %d: %s'%(i, sol(s)))