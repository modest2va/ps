import sys
from collections import deque

n=int(input())
commands=deque()
for i in range(n):
    command = sys.stdin.readline().rstrip()
    if command =='front':
        if len(commands) ==0 :
            print(-1)
        else:
            print(commands[0])
    elif command =='back':
        if len(commands) ==0 :
            print(-1)
        else:
            print(commands[-1])
    elif command =='empty':
        if len(commands) ==0 :
            print(1)
        else:
            print(0)
    elif command == 'size':
        print(len(commands))
    elif command == 'pop':
        if len(commands) ==0 :
            print(-1)
        else:
            print(commands.popleft())
    else:
        push, num= command.split()
        commands.append(int(num))