def sol(s):
    len_s = len(s)
    strings = []
    for i in range(1, len_s - 1):
        for j in range(1, len_s - 1):
            if i + j <= len_s - 1:
                strings.append(s[:i][::-1] + s[i:i + j][::-1] + s[i + j:][::-1])
    return(sorted(strings)[0])

s=input()
print(sol(s))