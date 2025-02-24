#9076

t = int(input())

for i in range(t):
  score_list = list(map(int, input().split()))
  score_list.sort()
  if score_list[3] - score_list[1] >= 4:
    print('KIN')
  else:
    print(score_list[1] + score_list[2] + score_list[3])