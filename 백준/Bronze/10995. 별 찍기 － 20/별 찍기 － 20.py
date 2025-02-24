def odd_line(n):
    for i in range(1,2*n):
        if i%2==1 :
            print('*',end='')
        else : print(' ',end='')
def even_line(n):
    for i in range(1,2*(n+1)):
        if i%2==1 :
            print(' ',end='')
        else : print('*',end='')
n=int(input())
for i in range(1,n+1):
    if i%2==1 :
        odd_line(n)
    else :
        even_line(n)
    print()