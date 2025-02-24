def sol(n):
    start_num = int(n)
    num_check =[]
    while True:
        check_num =0

        for i in n:
            check_num+=int(i)**2
        n = check_num
        if n == 1:
            return 'HAPPY'
        elif n in num_check:
            return 'UNHAPPY'
        num_check.append(n)
        n = str(n)

if __name__ == '__main__':
    n=input()
    print(sol(n))
