def sol(semina):
    room_number = {
        'Algorithm' : '204',
        'DataAnalysis': '207',
        'ArtificialIntelligence': '302',
        'CyberSecurity': 'B101',
        'Network': '303',
        'Startup': '501',
        'TestStrategy': '105'
    }

    return room_number[semina]


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(sol(input()))