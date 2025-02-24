def sol(patty, cheese):
    if patty > cheese:
        return 2 * cheese + 1
    elif patty == cheese:
        return 2 * cheese - 1
    else:
        return 2 * patty - 1


if __name__ == '__main__':
    patty, cheese = map(int, input().split())
    print(sol(patty, cheese))
