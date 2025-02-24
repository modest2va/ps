import sys
if __name__ == '__main__':

    tmp = int(sys.stdin.readline())
    for _ in range(tmp):
        n = int(sys.stdin.readline())
        if n == 1:
            print("#")
        elif n == 2:
            print("##")
            print("##")
        else:
            print("#" * n)
            for j in range(n - 2):
                print("#" + "J" * (n - 2) + "#")
            print("#" * n)
        if _ != tmp-1:
            print()