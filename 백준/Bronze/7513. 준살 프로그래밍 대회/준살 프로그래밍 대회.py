t = int(input())

for i in range(t):
    m = int(input())
    words = []
    for j in range(m):
        words.append(input())
    n = int(input())
    print(f'Scenario #{i + 1}:')
    for j in range(n):
        password = ''
        word_position = list(map(int, input().split()))
        for k in range(1, len(word_position)):
            password += words[word_position[k]]
        print(password)
    print()