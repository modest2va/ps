def sol(s):
    name = {
        'NLCS':'North London Collegiate School',
        'BHA': 'Branksome Hall Asia',
        'KIS': 'Korea International School',
        'SJA': 'St. Johnsbury Academy'
    }
    if s in name:
        return name[s]

if __name__ == '__main__':
    s = input()
    print(sol(s))
