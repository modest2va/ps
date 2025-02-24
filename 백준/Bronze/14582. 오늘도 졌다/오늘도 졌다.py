jeminis=list(map(int, input().split()))
gullivers=list(map(int, input().split()))

jem_scores=0
gull_scores=0
flag=0
for i in range(9):
    jem_scores += jeminis[i]
    if jem_scores>gull_scores:
        flag=1    
    gull_scores += gullivers[i]
if flag == 1 and jem_scores <gull_scores:
    print("Yes")
else:
    print("No")