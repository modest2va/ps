def sol(a, b, k, x):
    answer = min(k + x, b) - max(a, k - x) + 1
    if answer >= 0:
        return answer
    else:
        return 'IMPOSSIBLE'

if __name__ == '__main__':
    a, b = map(int, input().split())
    k, x = map(int, input().split())
    print(sol(a, b, k, x))
