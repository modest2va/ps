from math import ceil
def sol(a, b):
    answer = ceil((a*b)/4840/5)
    return answer

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(sol(a, b))
    