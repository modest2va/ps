def sol(s):
    s = list(reversed(s.split()))
    for i in range(len(s)):
        s[i]=s[i][::-1]
    answer = ' '.join(s)
    return answer
if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        s = input()
        print(sol(s))
