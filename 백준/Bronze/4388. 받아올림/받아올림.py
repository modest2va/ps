def sol(n1, n2):
    n1 = n1.zfill(max(len(n1), len(n2)))[::-1]
    n2 = n2.zfill(max(len(n1), len(n2)))[::-1]
    answer = 0
    carry = 0
    for i in range(len(n1)):
        if int(n1[i]) + int(n2[i]) + carry >= 10:
            answer += 1
            carry = 1
        else:
            carry = 0
    return answer


if __name__ == '__main__':

    while True:
        n1, n2 = input().split()
        if n1 == '0' and n2 == '0':
            break
        print(sol(n1, n2))
