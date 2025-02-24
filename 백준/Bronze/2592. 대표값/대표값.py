from collections import Counter
tmp=[]
for i in range(10):
    tmp.append(int(input()))
print(sum(tmp)//10)
cnt=Counter(tmp)
print(cnt.most_common(1)[0][0])