from itertools import permutations

def is_pal(words):
    if (words[0] + words[1]) == (words[0] + words[1])[::-1]:
        return words[0] + words[1]
    else:
        return False
def sol(word_list):
    per = list(permutations(word_list, 2))
    for test in per:
        if is_pal(test):
            return is_pal(test)
    return 0

t = int(input())

for i in range(t):
    k = int(input())
    word_list = [input() for x in range(k)]
    print(sol(word_list))