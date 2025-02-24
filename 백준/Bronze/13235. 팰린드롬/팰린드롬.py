def sol(s):
    if s.lower() == s[::-1].lower():
        return 'true'
    else:
        return 'false'
s = input()
print(sol(s))