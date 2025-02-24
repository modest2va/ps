import sys
from collections import Counter
n=int(sys.stdin.readline())
cards=list(map(int, sys.stdin.readline().split()))
m=int(sys.stdin.readline())
to_find=list(map(int, sys.stdin.readline().split()))

counter_cards = Counter(cards)
for i in to_find:
    #if i!=to_find[-1]:
        print(counter_cards[i], end=' ')
    # else:
    #     print(counter_cards[i], end='')

#print(counter_cards)