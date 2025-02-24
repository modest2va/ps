def sol(n):
    cnt = 0
    while n != 6174:
        str_num=str(n).zfill(4)
        min_number = ''.join(sorted(list(str_num)))
        max_number = ''.join(sorted(list(str_num), reverse=True))
        n = int(max_number) - int(min_number)
        cnt+=1
    return cnt


t= int(input())
for i in range(t):
    n=int(input())
    print(sol(n))