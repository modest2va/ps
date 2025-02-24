import sys
n=int(input())
pg=list(map(int,sys.stdin.readline().split()))
print(min (pg[ :pg.index(-1)])+min(pg[pg.index(-1)+1:]))