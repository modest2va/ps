def sol(a):
    pi = 3.141592
    r = (a/pi)**(1/2)
    answer = 2*pi*r
    return answer

if __name__ == '__main__':
    a= int(input())
    print(sol(a))