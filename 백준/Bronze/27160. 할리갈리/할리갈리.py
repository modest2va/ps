if __name__ == '__main__':
    n = int(input())
    hali = {"STRAWBERRY":0
            , "BANANA":0
            , "LIME":0
            , "PLUM":0
            }
    for i in range(n):
        fruit, cnt = input().split()
        cnt = int(cnt)
        hali[fruit] += cnt

    exist = any(value == 5 for value in hali.values())

    if exist:
        print("YES")
    else:
        print("NO")