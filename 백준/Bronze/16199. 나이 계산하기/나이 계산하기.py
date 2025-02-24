birthYear,birthMonth,birthDay=map(int,input().split())
currentYear, currentMonth, currentDay = map(int, input().split())
if currentMonth>birthMonth : ageFirst=currentYear-birthYear
elif currentMonth<birthMonth : ageFirst=currentYear-birthYear-1
else :
   if currentDay>=birthDay : ageFirst= currentYear-birthYear
   else: ageFirst=currentYear-birthYear-1
ageSecond= currentYear-birthYear +1
ageThird=currentYear-birthYear
print(ageFirst)
print(ageSecond)
print(ageThird)