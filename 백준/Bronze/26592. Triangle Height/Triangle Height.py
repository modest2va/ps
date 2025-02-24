def sol(a, b):
    answer = 2*a/b
    return answer

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        a, b = map(float, input().split())
        print('The height of the triangle is %.2f units'%sol(a, b))
