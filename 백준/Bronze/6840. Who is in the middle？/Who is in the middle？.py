def sol(bears):

    return sum(bears) - (max(bears)+min(bears))

if __name__ == '__main__':
    bears = []
    bears.append(int(input()))
    bears.append(int(input()))
    bears.append(int(input()))

    print(sol(bears))