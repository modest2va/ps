t = int(input())
for i in range(t):
    s1, s2 = input().split()
    answer = []
    for j in range(len(s1)):
        if ord(s2[j]) < ord(s1[j]) :
            answer.append(str(ord(s2[j]) + 26 - ord(s1[j])))
        else:
            answer.append(str(ord(s2[j]) - ord(s1[j])))
    print('Distances:', ' '.join(answer))