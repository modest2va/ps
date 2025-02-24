def sol(seminar_list):
    seminar_list.sort(key=lambda x: -int(x[1]))
    return seminar_list[0][0]


if __name__ == '__main__':
    seminar_list = [input().split() for i in range(7)]
    print(sol(seminar_list))
