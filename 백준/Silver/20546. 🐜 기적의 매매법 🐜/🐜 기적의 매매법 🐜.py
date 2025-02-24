def bnp(cash, stocks):
    current_stocks=0
    for current_price in stocks:
        current_stocks += cash//current_price
        cash-= (cash//current_price)*current_price
    total = cash+ current_stocks * stocks[-1]
    return total

def timing(cash, stocks):
    current_stocks=0
    for i in range(len(stocks)-3):
        if stocks[i+2]< stocks[i+1]< stocks[i]:
            current_stocks+=cash//stocks[i+3]
            cash %= stocks[i+3]
        elif stocks[i+2]> stocks[i+1]> stocks[i]:
            cash += stocks[i + 3] *current_stocks
            current_stocks=0
    total = cash+ current_stocks * stocks[-1]
    return total

if __name__ == '__main__':
    cash = int(input())
    stocks = list(map(int, input().split()))
    if bnp(cash,stocks)>timing(cash, stocks):
        print("BNP")
    elif bnp(cash, stocks) < timing(cash, stocks):
        print("TIMING")
    else:
        print("SAMESAME")
