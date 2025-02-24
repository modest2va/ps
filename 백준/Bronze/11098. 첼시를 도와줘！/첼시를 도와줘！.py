for _ in range(int(input())):
    price,name=0,'Daniel'
    for i in range(int(input())):
        a,b=input().split()
        a=int(a)
        if price<a: name=b; price=a
    print(name)