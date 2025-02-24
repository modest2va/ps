n = int(input())
chicken_list = list(map(int, input().split()))
total = 0
for i_want in chicken_list:
    if i_want > n:
        total += n
    else:
        total += i_want

print(total)