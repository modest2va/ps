def returnIncome(income):
    if income>5000000 : taxed= int(income*0.2)
    elif income > 1000000: taxed = int(income * 0.1)
    else : taxed = 0
    return (income-taxed)

while 1:
    income=int(input())
    if income==0: break
    else: print(returnIncome(income))