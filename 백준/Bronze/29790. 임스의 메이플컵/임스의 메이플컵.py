def sol(n, u, l):
    if n >= 1000 and (u >=8000 or l>=260):
        return 'Very Good'
    elif n >= 1000:
        return 'Good'
    else:
        return 'Bad'

if __name__ == '__main__':
    n, u, l = map(int, input().split())
    print(sol(n, u, l))