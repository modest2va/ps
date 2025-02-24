def sol(a, b):
    answer = max(a,b) - min(a,b)
    return answer

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        a, b = map(float, input().split())
        print('%.1f'%sol(a, b))