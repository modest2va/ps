def sol(s):
    circle = {
        'M' : 'MatKor',
        'W' : 'WiCys',
        'C' : 'CyKor',
        'A' : 'AlKor',
        '$' : '$clear',
    }
    return circle[s]

if __name__ == '__main__':
    s = input()
    print(sol(s))