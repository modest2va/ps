def sol(s):
    answer = len(s) + s.count(':') + s.count('_') * 5
    return answer


if __name__ == '__main__':
    s = input()
    print(sol(s))