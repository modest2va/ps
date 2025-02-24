while True:
    s = input()
    if s == '0':
        break
    digital_root = int(s)
    while digital_root > 9:
        digital_root=0
        for i in s:
            digital_root += int(i)
        s = str(digital_root)
    print(digital_root)