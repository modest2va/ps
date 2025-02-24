a, b = input().split()
my_min = int(a.replace('6', '5')) + int(b.replace('6', '5'))
my_max = int(a.replace('5', '6')) + int(b.replace('5', '6'))

print(my_min, my_max)
