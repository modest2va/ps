if __name__ == '__main__':
    n = int(input())
    s = ['Never gonna give you up',
         'Never gonna let you down',
         'Never gonna run around and desert you',
         'Never gonna make you cry',
         'Never gonna say goodbye',
         'Never gonna tell a lie and hurt you',
         'Never gonna stop']
    answer = 'No'
    for i in range(n):
        sentence = input()
        if sentence not in s:
            answer = 'Yes'
    print(answer)