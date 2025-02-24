def sol(w, h):
    return w * h /2

if __name__ == '__main__':
    w, h = map(int,input().split())
    print(f'{sol(w,h):.1f}')