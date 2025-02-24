s=input()
n=len(s)//2
for _ in range(n):
    s=s.replace("()","")
print(len(s))