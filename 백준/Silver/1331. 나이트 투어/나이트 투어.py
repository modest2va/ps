start = input()
x, y = ord(start[0])-64, int(start[1])
ways=[start]
flag = 0
for i in range(36):
    if i !=35:
        arrived= input()
    else:
        arrived = start
    x_arrived, y_arrived = ord(arrived[0]) - 64, int(arrived[1])

    if arrived in ways and i!=35:
        flag = 1
    if (abs(x-x_arrived)==2 and abs(y-y_arrived)==1) or (abs(y-y_arrived)==2 and abs(x-x_arrived)==1):
        pass
    else:
        flag = 1
    ways.append(arrived)
    x, y= x_arrived, y_arrived
if flag==1:
    print("Invalid")
else:
    print("Valid")