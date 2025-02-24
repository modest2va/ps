from collections import deque
for i in range(int(input())):
    n, m = map(int, input().split())
    waiting= deque(list(map(int,input().split())))
    importance = deque(list([i for i in range(n)]))
    cnt = 0
    while waiting:
        if waiting[0] == max(waiting):
            cnt+=1
            waiting.popleft()
            if importance.popleft() == m:
                print(cnt)

        else:
            waiting.append(waiting.popleft())
            importance.append(importance.popleft())