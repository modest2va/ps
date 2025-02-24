A,B=map(int,input().split())
C=int(input())

print ("%d %d" %(int ( (A+ int ((B+C)/60)))%24,(B+C)%60))