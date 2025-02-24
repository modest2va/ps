def sol(s,n):
    answer = [s]
    while True:
        s = str(int(s)**2).zfill(n*2)
        s = s[n//2:2*n-n//2]
        if s not in answer:
            answer.append(s)
        else:
            return len(answer)

if __name__ == '__main__':
    while True:
        s = input()
        n = 4
        if s == '0':
            break
        print(sol(s,n))
