def sol(s):
    cnt_security = s.count('security')
    cnt_bigdata= s.count('bigdata')
    if cnt_security>cnt_bigdata:
        return 'security!'
    elif cnt_security<cnt_bigdata:
        return 'bigdata?'
    else:
        return 'bigdata? security!'

if __name__ == '__main__':
    n = int(input())
    s = input()
    print(sol(s))