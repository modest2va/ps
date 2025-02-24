def baekjoon_17202(gunghap):
    new_gunghap = ''
    for i in range(len(gunghap) - 1):
        new_gunghap += str((int(gunghap[i])+int(gunghap[i+1]))% 10)
    if len(new_gunghap)>2:
        return baekjoon_17202(new_gunghap)
    return new_gunghap

phone1 = input()
phone2 = input()
gunghap = ''
for i in range(8):
    gunghap += phone1[i]
    gunghap += phone2[i]
print(baekjoon_17202(gunghap))