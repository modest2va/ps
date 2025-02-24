n = int(input())
s = input()
list_s =[]
for i in range(len(s)//n):
    if i % 2 ==0 :
        list_s.append(s[n*i:n*(i+1)])
    else:
        list_s.append(s[n * i:n * (i + 1)][::-1])
answer = ''
for i in range(n):
    for j in range(len(s)//n):
        answer += list_s[j][i]
print(answer)