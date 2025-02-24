import sys
def cal(a,b,c,d):
    return abs(c-a)+abs(d-b)
n = int(sys.stdin.readline())
distance_list=[]
start_x, start_y, end_x, end_y = map(int, sys.stdin.readline().split())
for i in range(n):
    m=int(sys.stdin.readline())
    go_x, go_y = start_x, start_y
    sum_distance=0
    for j in range(m):
        arrive_x, arrive_y = map(int, sys.stdin.readline().split())
        sum_distance+=cal(go_x, go_y, arrive_x, arrive_y)
        go_x, go_y = arrive_x, arrive_y
    sum_distance += cal(go_x, go_y, end_x, end_y)
    go_x, go_y = end_x, end_y
    distance_list.append(sum_distance)

print(distance_list.index(min(distance_list))+1)