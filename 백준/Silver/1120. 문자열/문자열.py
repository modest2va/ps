def sol(a, b):
    distances = []
    for i in range(len(b) - len(a) + 1):
        distance = 0
        for j in range(len(a)):
            if a[j] != b[i + j]:
                distance += 1
        distances.append(distance)
    return min(distances)

a, b = input().split()
print(sol(a, b))

