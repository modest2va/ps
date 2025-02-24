def sol(s_list):
    answer = [x[0] for x in s_list]
    if len(set(answer)) == 1:
        return 1
    else:
        return 0

n = int(input())
words = input().split()
print(sol(words))