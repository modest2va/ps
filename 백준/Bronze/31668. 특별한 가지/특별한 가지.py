def sol(n, m, k):
    answer = (m // n) * k
    return answer


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    k = int(input())
    print(sol(n, m, k))
