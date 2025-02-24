n = int(input())
s = input()
hidden_list = [0]
hidden_number = '0'
for i in s:
    if i.isdigit():
        hidden_number += i
    else:
        hidden_list.append(int(hidden_number))
        hidden_number = '0'
if hidden_number != '0':
    hidden_list.append(int(hidden_number))

print(sum(hidden_list))