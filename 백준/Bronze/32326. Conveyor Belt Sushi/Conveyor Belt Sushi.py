def sol(r, g, b):
    red_plate_cost = 3
    green_plate_cost = 4
    blue_plate_cost = 5

    return r * red_plate_cost + g * green_plate_cost + b * blue_plate_cost


if __name__ == '__main__':
    r = int(input())
    g = int(input())
    b = int(input())

    print(sol(r, g, b))
