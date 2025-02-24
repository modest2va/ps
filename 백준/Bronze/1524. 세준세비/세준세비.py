from sys import stdin
from collections import deque
def sol(sejun, sebi):
    answer = 'C'

    while len(sejun)!=0 and len(sebi)!=0:
        if sejun[0]<sebi[0]:
            sejun.popleft()
        else :
            sebi.popleft()
    if len(sejun)>len(sebi):
        answer = 'S'
    elif len(sebi)>len(sejun):
        answer = 'B'
    return answer


if __name__ == '__main__':
    t= int(input())
    for i in range(t):
        blank = input()
        n, m= map(int,stdin.readline().split())
        sejun = deque(map(int,stdin.readline().split()))
        sebi = deque(map(int, stdin.readline().split()))
        print(sol(sejun,sebi))
