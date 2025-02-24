def solution(s):
    zeros =s.split('0')
    ones = s.split('1')
    cnt_ones = cnt_zeros = 0
    for i in zeros:
        if i != '':
            cnt_ones += 1
    for i in ones:
        if i != '':
            cnt_zeros += 1

    return min(cnt_zeros,cnt_ones)


s = input()
print(solution(s))
