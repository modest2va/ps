import sys
for i in range(1,int(sys.stdin.readline())+1):
    tmp=sorted(map(int, sys.stdin.readline().split()))
    if tmp[0]+tmp[1]<=tmp[2]: s="invalid!"
    elif tmp[0]==tmp[1]== tmp[2]: s="equilateral"
    elif tmp[0]==tmp[1] or tmp[1]==tmp[2] : s="isosceles"
    else : s="scalene"
    print ("Case #%d: %s"%(i,s))