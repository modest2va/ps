def sol(s):
    answer = ''.join(sorted(s,reverse=True))
    return answer

if __name__ == '__main__':
    s = input()
    print(sol(s))