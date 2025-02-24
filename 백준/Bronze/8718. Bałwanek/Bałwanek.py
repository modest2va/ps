def sol(n,k):
    answer =[]
    n= n*1000
    k= k*1000
    answer = 0
    answer_list = [k+k*2+k*4,int(k/2+k+2*k),int(k/4+k/2+k)]
    for i in answer_list:
        if i<=n:
            answer = i
            break
    return answer
if __name__ == '__main__':
    n, k = map(int, input().split())
    print(sol(n,k))
