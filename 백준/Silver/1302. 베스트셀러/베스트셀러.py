from collections import Counter
# tmp=[1,1,1,2,3,5,5]
# counter_tmp=Counter(tmp)
# print(counter_tmp.most_common(n=1)[0][0])

n=int(input())
tmp=[]
for i in range(n):
    tmp.append(input())
tmp.sort()
counter_tmp=Counter(tmp)
print(counter_tmp.most_common(n=1)[0][0])