def ascii_art(r,g,b):
    intensity = 2126*r+7152*g+722*b
    if intensity<510_000:
        return '#'
    elif intensity<1_020_000:
        return 'o'
    elif intensity<1_530_000:
        return '+'
    elif intensity<2_040_000:
        return '-'
    else:
        return '.'

if __name__ == '__main__':
    n, m = map(int, input().split())
    for _ in range(n):
        nums = list(map(int,input().split()))
        changed = []
        for i in range(m):
            changed.append(ascii_art(nums[3*i], nums[3*i+1], nums[3*i+2]))
        print(''.join(changed))