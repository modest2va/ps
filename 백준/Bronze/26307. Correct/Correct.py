def sol(hh, mm):
    answer = hh*60 + mm - 9*60
    return answer

if __name__ == '__main__':
    hh, mm = map(int, input().split())
    print(sol(hh, mm))
