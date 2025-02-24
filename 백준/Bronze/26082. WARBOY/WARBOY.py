def sol(a,b,c):
    answer = int(b/a)*3*c
    return answer

if __name__ == '__main__':
    a, b, c= map(int, input().split())
    print(sol(a,b,c))