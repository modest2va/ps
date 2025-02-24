a=int(input())
x=int(input())
b=int(input())
y=int(input())
t=int(input())
if t>30: ans= a+((t-30)*x)*21
else: ans=a
if t>45: ans2= b+((t-45)*y)*21
else: ans2=b
print(ans, ans2)