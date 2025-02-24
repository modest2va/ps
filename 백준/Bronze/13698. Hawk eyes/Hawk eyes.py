if __name__ == '__main__':
    change = input()
    changes = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]
    cups = ['small', 'X', 'X', 'big']
    for c in change:
        type_change = ord(c) - 65
        start, end = changes[type_change][0], changes[type_change][1]
        cups[start], cups[end] = cups[end], cups[start]

    print(cups.index('small') + 1)
    print(cups.index('big') + 1)
