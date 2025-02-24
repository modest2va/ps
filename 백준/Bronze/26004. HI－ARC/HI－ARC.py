def sol(s):
    h,i,a,r,c = s.count('H'),s.count('I'),s.count('A'),s.count('R'),s.count('C')
    answer = min(h,i,a,r,c)
    return answer


if __name__ == '__main__':
    n = int(input())
    s = input()
    print(sol(s))