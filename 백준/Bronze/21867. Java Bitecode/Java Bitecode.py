def sol(s):
    to_be_changed = 'JAV'
    for alphabet in to_be_changed :
        s = s.replace(alphabet, '')
    if len(s) == 0:
        return 'nojava'
    else:
        return s

if __name__ == '__main__':
    len_s = int(input())
    s = input()
    print(sol(s))
