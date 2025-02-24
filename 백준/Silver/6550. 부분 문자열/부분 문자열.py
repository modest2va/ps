def sol(s, t):
    check = 0
    for i in t:
        if s[check] == i:
            check += 1
        if check == len(s):
            return 'Yes'



    return 'No'


if __name__ == '__main__':

    while True:
        try:
            s, t = input().split()
            print(sol(s,t))
        except:
            break