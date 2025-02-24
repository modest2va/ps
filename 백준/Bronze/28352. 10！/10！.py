from math import factorial
def sol(n):
    one_week = 7 *24*60*60
    return factorial(n)//one_week

if __name__ == '__main__':
    n = int(input())
    print(sol(n))