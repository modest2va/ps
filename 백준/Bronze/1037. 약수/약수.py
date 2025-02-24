n=int(input())
tmp=list(map(int, input().split()))
tmp=sorted(tmp)
print(tmp[0]*tmp[-1])