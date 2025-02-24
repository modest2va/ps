def sol(milk_shop):
    answer = 0
    current_milk = 0
    for milk in milk_shop:
        if current_milk == milk:
            answer += 1
            #current_milk = (current_milk + 1) % 3
            current_milk += 1
            if current_milk >=3 :
                current_milk -= 3
    return answer

n = int(input())
milk_shop = list(map(int, input().split()))
print(sol(milk_shop))