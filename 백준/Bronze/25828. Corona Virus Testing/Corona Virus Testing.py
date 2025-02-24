def sol(g,p,t):
    origin = g * p
    new = g + p * t
    if origin < new:
        return 1
    elif origin > new:
        return 2
    else:
        return 0

if __name__ == '__main__':
    g, p, t = map(int, input().split())
    print(sol(g, p, t))
