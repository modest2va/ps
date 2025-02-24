def sol(n):
    answer = []
    while n >=5:
        answer.append('++++')
        n -= 5
    if n>=1:
        answer.append('|'*n)

    return answer
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(' '.join(sol(n)))