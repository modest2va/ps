def sol(apple, banana):
    end = min(apple,banana) +1

    for i in range(1, end):
        if apple%i == 0 and banana%i == 0 :
            print(i, apple//i, banana//i)



if __name__ == '__main__':
    apple, banana = map(int, input().split())
    sol(apple, banana)
