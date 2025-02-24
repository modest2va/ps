def sol(s):
    answer = s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')

    return answer


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        s = input()
        print('The number of vowels in %s is %d.' % (s, sol(s)))
