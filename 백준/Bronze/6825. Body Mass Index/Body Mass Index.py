def sol(weight, height):
    bmi = weight/(height**2)
    if bmi>25:
        return 'Overweight'
    elif bmi>=18.5:
        return 'Normal weight'
    else:
        return 'Underweight'

if __name__ == '__main__':
    weight = float(input())
    height = float(input())
    print(sol(weight, height))
    