n = int(input())
for i in range(n):
    s1 = input()
    s2 = input()
    answer = 0
    for j in range(len(s1)):
        if s1[j] != s2[j]:
            answer += 1
    print(f'Hamming distance is {answer}.')
    