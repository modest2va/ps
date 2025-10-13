def sol(t):
    if (t + 0.5) % 25 <= 17:
        return "ONLINE"
    else:
        return "OFFLINE"

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        t = int(input())
        print(sol(t))