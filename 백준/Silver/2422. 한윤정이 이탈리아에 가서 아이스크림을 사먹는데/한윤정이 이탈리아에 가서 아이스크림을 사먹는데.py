if __name__ == '__main__':
    n, m=map(int,input().split())
    icecream=[[True for i in range(n)] for i in range(n)]
    for i in range(m):
        flavor_one, flavor_two = map(int,input().split())
        icecream[flavor_one-1][flavor_two-1] = False
        icecream[flavor_two - 1][flavor_one - 1] = False
    answer = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j + 1, n):
              if icecream[i][j] and icecream[j][k] and icecream[i][k]:
                  answer+=1
    print(answer)