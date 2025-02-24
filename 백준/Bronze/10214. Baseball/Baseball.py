for i in range(int(input())):
    yonsei,korea=0,0
    for _ in range(9):
        a,b=map(int, input().split())
        yonsei+=a; korea+=b
    if yonsei>korea:print("Yonsei")
    elif yonsei==korea:print("Draw")
    else: print("Korea")