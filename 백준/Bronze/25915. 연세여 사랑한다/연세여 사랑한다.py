def sol(c, yonsei):
    answer = 0
    yonsei.insert(0,c)
    for i in range(1,len(yonsei)):
        answer+=abs(ord(yonsei[i])-ord(yonsei[i-1]))

    return answer
if __name__ == '__main__':
    c =input()
    yonsei = (list('ILOVEYONSEI'))
    print(sol(c,yonsei))