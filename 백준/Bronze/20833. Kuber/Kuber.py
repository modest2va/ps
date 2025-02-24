def sol(n):
    answer = 0
    for i in range(1,n+1):
        answer+=i**3
    return answer
if __name__ == '__main__':
    n = int(input())
    print(sol(n))