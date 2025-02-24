def sol(a,b,c):
    answer = '*'
    if a!=b and a!=c:
        return 'A'
    elif b!=a and b!=c:
        return 'B'
    if c!=a and c!=b:
        return 'C'
    return answer

if __name__ == '__main__':
    a, b, c =map(int, input().split())
    print(sol(a,b,c))