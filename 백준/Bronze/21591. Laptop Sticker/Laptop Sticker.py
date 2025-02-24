def sol(wc, hc, ws, hs):
    answer = 0
    if wc-ws >1 and hc-hs >1 :
        answer = 1
    return answer

if __name__ == '__main__':
    wc, hc, ws, hs = map(int, input().split())
    print(sol(wc, hc, ws, hs))