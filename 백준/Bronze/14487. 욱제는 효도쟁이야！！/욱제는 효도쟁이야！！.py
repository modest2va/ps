def sol(distances):
    return sum(distances) - max(distances)


n = int(input())
distances = list(map(int, input().split()))

print(sol(distances))
