s = input()

answer = 'YES'
mobis = 'MOBIS'
for i in mobis:
    if i not in s:
        answer = 'NO'
print(answer)