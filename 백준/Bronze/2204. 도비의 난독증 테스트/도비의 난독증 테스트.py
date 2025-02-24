# print(ord('C'))
# print(ord('b'))
while True:
    n = int(input())
    if n == 0:
        break
    words = [input() for i in range(n)]
    new_words = [i.lower() for i in words]

    answer = new_words.index(min(new_words))
    print(words[answer])