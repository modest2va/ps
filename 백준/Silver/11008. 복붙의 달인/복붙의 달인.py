def sol(origin_string, clipboard_string):
    origin_string = origin_string.replace(clipboard_string,'*')
    return len(origin_string)

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        origin_string, clipboard_string = input().split()
        print(sol(origin_string, clipboard_string))