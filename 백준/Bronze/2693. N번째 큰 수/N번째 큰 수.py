# 2693

t = int(input())
for i in range(t):
    my_list = list(map(int, input().split()))
    my_list.sort(reverse = True)
    print(my_list[2])