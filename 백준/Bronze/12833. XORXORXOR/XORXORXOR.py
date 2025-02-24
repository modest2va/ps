def sol(a,b,c):
    answer = a
    if c%2 == 1:
        answer = a^b
    return answer
if __name__ == '__main__':
    a,b,c = map(int, input().split())
    print(sol(a,b,c))