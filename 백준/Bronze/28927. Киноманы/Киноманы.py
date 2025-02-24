def sol(movie1, movie2):
    max_total = movie1[0] * 3 + movie1[1] * 20 + movie1[2] * 120
    mel_total = movie2[0] * 3 + movie2[1] * 20 + movie2[2] * 120
    if max_total > mel_total:
        print('Max')
    elif max_total < mel_total:
        print('Mel')
    else:
        print('Draw')


if __name__ == '__main__':
    movie1 = list(map(int, input().split()))
    movie2 = list(map(int, input().split()))
    sol(movie1, movie2)
