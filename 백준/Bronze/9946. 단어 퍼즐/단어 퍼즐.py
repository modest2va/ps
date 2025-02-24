start = 1
while True:
    s1 = (input())
    s2 = (input())

    if s1 == 'END' and s2 == 'END':
        break
    if sorted(list(s1)) == sorted(list(s2)):
        print(f'Case {start}: same')
    else:
        print(f'Case {start}: different')
    start +=1 