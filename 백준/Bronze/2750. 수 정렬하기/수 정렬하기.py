# 2750
n = int(input())
my_list = []

for i in range(n):
  num = int(input())
  my_list.append(num)
my_list.sort()

for i in my_list:
  print(i)