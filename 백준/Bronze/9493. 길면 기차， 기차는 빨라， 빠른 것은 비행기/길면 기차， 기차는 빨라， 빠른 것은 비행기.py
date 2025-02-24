import sys
while True:
    m,a,b=map(int, sys.stdin.readline().split())
    if m==a==b==0: break
    sec=(m*( (b-a)/(a*b))*3600)
    h= int (sec//3600)
    mm= int (sec%3600)//60
    ss= round ((sec%3600)%60 , 0)
    print("%.1d:%.2d:%.2d"%(h,mm,ss))