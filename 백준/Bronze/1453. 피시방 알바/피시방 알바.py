pc_rooms = [0] * 101

n = int(input())
customer = list(map(int, input().split()))
answer = 0
for i in customer:
    if pc_rooms[i] == 0:
        pc_rooms[i] = 1
    else:
        answer += 1
print(answer)