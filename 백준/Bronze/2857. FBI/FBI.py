fbi_list = []
for i in range(5):
    s = input()
    if 'FBI' in s:
        fbi_list.append(i + 1)
fbi_list.sort()
if len(fbi_list) == 0:
    print('HE GOT AWAY!')
else:
    for i in fbi_list:
        print(i, end = ' ')