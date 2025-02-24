students = [0] * 31

for i in range(28):
    homework = int(input())
    students[homework] = 1

for i in range(1, 31):
    if students[i] == 0:
        print(i)
        