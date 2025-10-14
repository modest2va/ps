if __name__ == '__main__':
    seconds = 300
    for i in range(4):
        seconds += int(input())

    if seconds > 1800:
        print("No")

    else:
        print("Yes")