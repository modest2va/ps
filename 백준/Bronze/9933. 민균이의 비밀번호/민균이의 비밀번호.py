n = int(input())
passwords = []
for i in range(n):
    s = input()
    passwords.append(s)

for i in passwords:
    if i[::-1] in passwords:
        print(len(i), i[len(i)//2])
        break