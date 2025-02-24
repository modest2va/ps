import sys
sys.setrecursionlimit(10**5)

def first(gunghap):
    alpha = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
    answer = ''
    for i in range(1, len(gunghap)):
        answer += str((alpha[ord(gunghap[i-1]) - 65] + alpha[ord(gunghap[i]) - 65])%10)

    return answer

def sol(gunghap):
    new_gunghap = ''
    for i in range(1, len(gunghap)):
        new_gunghap += str((int(gunghap[i-1]) + int(gunghap[i]))%10)
    if len(new_gunghap) > 2:
        return sol(new_gunghap)
    return new_gunghap

name1 = input()
name2 = input()

gunghap = ''
for i in range(len(name1)):
    gunghap += name1[i]
    gunghap += name2[i]
print(sol(first(gunghap)))