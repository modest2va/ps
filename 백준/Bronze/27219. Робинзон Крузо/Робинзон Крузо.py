def sol(n):
    answer = 'V' * (n // 5) + 'I' * (n % 5)
    return answer


if __name__ == '__main__':
    n = int(input())
    print(sol(n))
