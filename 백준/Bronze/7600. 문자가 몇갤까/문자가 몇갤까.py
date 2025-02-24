while 1:
    cnt=[0]*26
    s=str(input())
    if s=='#':break
    for i in s:
        if i.isalpha():
            i=i.lower()
            cnt[ord(i)-97]=1
    print(sum(cnt))