def sol(s):
    answer = ''
    for i in range(1,len(s)):
        if s[i-1]!=s[i]:
            answer +=s[i-1]
    return answer+s[-1]
if __name__ == '__main__':
    s = input()
    print(sol(s))
