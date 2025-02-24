def sol(a, b):
    if -a - int((a**2 -b)**0.5) == -a + int((a**2 -b)**0.5):
        return [-a - int((a**2 -b)**0.5)]
    else:
        return [-a - int((a**2 -b)**0.5), -a + int((a**2 -b)**0.5)]


a, b = map(int, input().split())

print(*sol(a, b))
