s = input()
vowel ='aeiou'
for i in vowel:
    s = s.replace(i+'p'+i, i)

print(s)