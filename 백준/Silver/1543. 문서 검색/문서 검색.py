def sol(s, target):
    answer = 0
    index = 0
    while index < len(s):
        position = s.find(target, index)
        if position == -1:
            break
        else:
            answer += 1
            index = position + len(target)

    return answer

s = input()
target = input()
print(sol(s, target))