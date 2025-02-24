from datetime import date, timedelta


def sol(n):
    start = date(2014, 4, 2)
    answer = start + timedelta(days=n - 1)
    return answer


if __name__ == '__main__':
    n = int(input())
    print(sol(n))
