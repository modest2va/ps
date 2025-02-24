def sol(i):
    s = "WelcomeToSMUPC"
    return s[(i-1)%14]
if __name__ == '__main__':
    i = int(input())
    print(sol(i))