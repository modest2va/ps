odd_numbers = []

for i in range(7):
    number = int(input())
    if number % 2 == 1:
        odd_numbers.append(number)

if odd_numbers:
    print(sum(odd_numbers))
    print(min(odd_numbers))
else:
    print(-1)