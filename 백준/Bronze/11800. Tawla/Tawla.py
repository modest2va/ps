def sol(n):
    if n == 1:
        return 'Yakk'
    elif n == 2:
        return 'Doh'
    elif n == 3:
        return 'Seh'
    elif n == 4:
        return 'Ghar'
    elif n == 5:
        return 'Bang'
    elif n == 6:
        return 'Sheesh'

if __name__ == '__main__':
    t = int(input())
    for i in range(1,t+1):
        a, b = map(int, input().split())
        first , second = sol(max(a,b)), sol(min(a,b))
        if a==b:
            if a == 1:
                print('Case %d: Habb Yakk'%(i))
            elif a == 2:
                print('Case %d: Dobara'%(i))
            elif a == 3:
                print('Case %d: Dousa'%(i))
            elif a == 4:
                print('Case %d: Dorgy'%(i))
            elif a == 5:
                print('Case %d: Dabash'%(i))
            elif a == 6:
                print('Case %d: Dosh'%(i))
        elif a+b== 11:
            print('Case %d: Sheesh Beesh'%(i))
        else:
            print('Case %d: %s %s'%(i, first, second))
