from math import ceil


def sol(s, a, b):
    answer = 250
    cost = 100
    if s <= a:
        return answer
    else:
        cnt = ceil((s - a) / b)
        return answer + cnt * cost


if __name__ == '__main__':
    s = int(input())
    a = int(input())
    b = int(input())
    print(sol(s, a, b))
