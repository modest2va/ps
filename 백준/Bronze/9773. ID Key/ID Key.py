def sol(s) -> int:
    first, last_three_number = 0, 0

    for i in s:
        first += int(i)
    last_three_number = int(s[-3] + s[-2] + s[-1]) * 10

    answer = first + last_three_number
    if first + answer < 1000:
        answer += 1000
    answer %= 10000
    return str(answer).zfill(4)


if __name__ == '__main__':
    for _ in range(int(input())):
        s = str(input())
        print(sol(s))
