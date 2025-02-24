from functools import lru_cache
siteDB={}
n,m=map(int, input().split())
for i in range(n):
    sitename,sitepw=input().split()
    siteDB[sitename]=sitepw
targetSite=[input() for i in range(m)]
for i in targetSite:
    print(siteDB[i])