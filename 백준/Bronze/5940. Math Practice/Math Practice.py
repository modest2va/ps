def sol(a, b):
    answer = 0
    for i in range(a+1, 63):
        if int(str(2**i)[0]) == b:
            return i

    return answer

if __name__ == '__main__':
    a, b= map(int, input().split())
    print(sol(a, b))