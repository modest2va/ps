t=int(input())
for _ in range(t):
    m,n=map(int,input().split())
    matrix=[list(map(int, input().split())) for i in range(m)]
    transposed_matrix=list(zip(*matrix))
    sum_distance_box=0
    for i in transposed_matrix:
        for j in range(1,m):
            if i[::-1][j]==1:
                sum_distance_box+=i[::-1][:j].count(0)
    print(sum_distance_box)