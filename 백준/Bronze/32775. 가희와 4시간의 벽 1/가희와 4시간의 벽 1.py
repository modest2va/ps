def sol(s_ab, f_ab):
    if s_ab > f_ab:
        return "flight"
    else:
        return "high speed rail"

if __name__ == '__main__':
    s_ab = int(input())
    f_ab = int(input())
    print(sol(s_ab, f_ab))