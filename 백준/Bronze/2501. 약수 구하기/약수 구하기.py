def solution(n, k):
    divisor = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisor.append(i)
            if i != n//i:
                divisor.append(n//i)
    divisor.sort()
    if len(divisor) < k:
        return 0
    else:
        return divisor[k -1]


if __name__ == '__main__':
    n, k = map(int, input().split())
    print(solution(n, k))
