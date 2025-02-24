t = int(input())
for i in range(t):
    n = int(input())
    rooms = [0] * (n+1)
    round = 1
    for j in range(1, n + 1):
        for k in range(len(rooms)):
            if k % j == 0:
                if rooms[k] == 0:
                    rooms[k] =1
                elif rooms[k] == 1:
                    rooms[k] = 0
    rooms[0] = 0
    print(sum(rooms))