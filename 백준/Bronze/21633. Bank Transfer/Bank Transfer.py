def sol(n):
    answer = 25 + n*0.01
    if answer >=2000:
        answer = 2000
    elif answer <=100:
        answer = 100
    return answer

if __name__ == '__main__':
    n = int(input())
    print("%.2f"%sol(n))