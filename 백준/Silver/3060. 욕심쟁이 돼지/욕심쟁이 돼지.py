def sol(food, pigs):
    total_sum =sum(pigs)
    days = 1
    while food>=total_sum:
        total_sum+=total_sum*3
        days+=1
    return days

if __name__ == '__main__':
    n=int(input())
    for i in range(n):
        food = int(input())
        pigs = list(map(int, input().split()))
        print(sol(food,pigs))