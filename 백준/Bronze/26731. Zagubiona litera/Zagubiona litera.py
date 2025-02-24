def sol(s):
    s = sorted(s)
    for i in range(len(s)):
        if i!= ord(s[i])-65:
            return chr(i+65)
    return 'Z'

if __name__ == '__main__':
    s = input()
    print(sol(s))
    