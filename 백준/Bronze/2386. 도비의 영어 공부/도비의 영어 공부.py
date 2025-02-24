while True:
    s = input().lower()
    if s == '#':
        break
    print(s[0], s.count(s[0])-1)