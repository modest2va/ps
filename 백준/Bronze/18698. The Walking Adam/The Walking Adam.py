def sol(steps):
    first_fall_down = steps.split("D")
    return len(first_fall_down[0])



if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        steps = input()
        print(sol(steps))