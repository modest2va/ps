m, n = map(int, input().split())
answer = ''
over_ten = 'ABCDEF'
if m == 0:
    print(0)
else:
    while m != 0 :
        if m % n >= 10:
            answer += over_ten[(m % n)%10]
        else:
            answer += str(m % n)
        m //= n
    print(answer[::-1])