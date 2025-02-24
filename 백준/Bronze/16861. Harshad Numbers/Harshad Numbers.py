def cal(n):
    answer = 0
    while n>0:
        answer+=n%10
        n//=10
    return answer
def sol(n):
    if n%cal(n) == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    n = int(input())
    while True:
        if sol(n):
            print(n)
            break
        else:
            n+=1
