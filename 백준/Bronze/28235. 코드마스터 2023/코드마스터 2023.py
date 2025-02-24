def sol(guho):
    guhos ={
        'SONGDO':'HIGHSCHOOL',
        'CODE': 'MASTER',
        '2023': '0611',
        'ALGORITHM': 'CONTEST'
    }
    return guhos[guho]

if __name__ == '__main__':
    s = input()
    print(sol(s))