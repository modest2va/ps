t = int(input())
for i in range(t):
    a, b= input().split()
    if sorted(list(a)) == sorted(list(b)):
        print(f'{a} & {b} are anagrams.')
    else:
        print(f'{a} & {b} are NOT anagrams.')