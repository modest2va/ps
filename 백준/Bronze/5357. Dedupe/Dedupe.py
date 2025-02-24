def sol(s):
    answer = [s[0]]
    for alphabet in s:
        if answer[-1] != alphabet:
            answer.append(alphabet)
    return ''.join(answer)

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        s = input()
        print(sol(s))
