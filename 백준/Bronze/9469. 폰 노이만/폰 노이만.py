import sys
for _ in range (int(sys.stdin.readline())):
    tmp=list (map(float, sys.stdin.readline().split()))
    print("%d %.6f"%(int(tmp[0]),tmp[4]*tmp[1]/(tmp[2]+tmp[3]) ))