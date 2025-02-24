def bunhaehap(n):
    hap = n
    while n > 0:
        hap += n % 10
        n //= 10

    return hap
def sol(n):
    answer = 0
    while bunhaehap(answer) != n:
        if answer == n:
            return 0
        else:
            answer += 1
    return answer

n = int(input())
print(sol(n))