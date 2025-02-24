if __name__ == '__main__':
    scores =[]
    n = int(input())
    for _ in range(n):
        a,d,g=map(int,input().split())
        score = a*(d+g)
        if a == (d+g):
            score*=2
        scores.append(score)
    print(max(scores))