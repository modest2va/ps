def sol(s):
    answer = 0
    vowels = ['a','e','i','o','u']
    for vowel in vowels:
        answer+=s.count(vowel)
    return answer

if __name__ == '__main__':
    len_s = int(input())
    s = input()
    print(sol(s))