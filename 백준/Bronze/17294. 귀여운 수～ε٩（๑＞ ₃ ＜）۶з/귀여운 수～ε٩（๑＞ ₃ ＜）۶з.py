n=input()
numbers=[]
for i in n:
    numbers.append(int(i))
cnt=1
for i in range(1,len(numbers)-1):
    if (numbers[i-1]+numbers[i+1])/2 != numbers[i] : cnt=0; print("흥칫뿡!! <(￣ ﹌ ￣)>"); break
if cnt==1:print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")