s=input()
cnt=0
two="ABC" ;three="DEF";four="GHI";five="JKL";six="MNO";seven="PQRS"
eight="TUV";nine="WXYZ"
for i in s:
    if i in two : cnt+=3
    if i in three: cnt += 4
    if i in four: cnt += 5
    if i in five: cnt += 6
    if i in six: cnt += 7
    if i in seven: cnt += 8
    if i in eight: cnt += 9
    if i in nine: cnt += 10
print(cnt)