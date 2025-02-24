import sys
cnt1=0; cnt2=0; cnt3=0;cnt4=0;cntax=0
for _ in range(int(sys.stdin.readline())):
    a,b=map(int, sys.stdin.readline().split())

    if a ==0 or b==0 : cntax+=1
    elif a>0 and b>0: cnt1+=1
    elif a < 0 and b > 0: cnt2 += 1
    elif a < 0 and b < 0: cnt3 += 1
    elif a > 0 and b < 0: cnt4 += 1

print("Q1: %d"%cnt1)
print("Q2: %d"%cnt2)
print("Q3: %d"%cnt3)
print("Q4: %d"%cnt4)
print("AXIS: %d"%cntax)