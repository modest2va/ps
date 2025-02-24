def print1(n):
    for i in range (n):
        print('@' * n + " " * 3 * n + '@' * n)
def print2(n):
    for i in range(n):
        print('@' * n*5)
n=int(input())
print1(n)
print2(n)
print1(n)
print2(n)
print1(n)