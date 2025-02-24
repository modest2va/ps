def sol(s1,s2):
    s1, s2 =sorted(s1), sorted(s2)
    if s1 == s2 :
        return 'Possible'
    else:
        return 'Impossible'

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        s1, s2 = map(str, input().split())
        print(sol(s1,s2))