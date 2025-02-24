def sol(w, h):
    diagonal = (w**2+h**2)**(1/2)
    answer = w+h - diagonal
    return answer

if __name__ == '__main__':
    w, h = map(int, input().split())
    print(sol(w, h))