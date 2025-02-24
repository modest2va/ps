def sol(start_num, target):
    target = str(target)
    answer = 0
    for i in range(1,start_num+1):
        answer += str(i).count(target)
    return answer

if __name__ == '__main__':
    start_num, target = map(int, input().split())
    print(sol(start_num, target))