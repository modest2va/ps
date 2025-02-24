VOWEL = 'aeiou'
s = input()
answer = 0
for i in VOWEL:
    answer += s.count(i)
print(answer)