if __name__ == '__main__':
    n, c = map(int,input().split())
    area_rooms = 0
    area_bedrooms = 0
    area_balcony = 0
    for _ in range(n):
        ai, ti = input().split()
        area_rooms += int(ai)
        if ti == 'bedroom':
            area_bedrooms += int(ai)
        if ti == 'balcony':
            area_balcony += int(ai)
    cost_flat = (area_rooms-(area_balcony/2))*c
    print(area_rooms)
    print(area_bedrooms)
    print(cost_flat)